import os
import warnings

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    make_scorer,
    mean_absolute_error,
    mean_squared_error,
    precision_score,
    r2_score,
    recall_score,
    roc_auc_score,
    silhouette_score,
)
from sklearn.model_selection import GridSearchCV, KFold, StratifiedKFold, cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor

warnings.filterwarnings("ignore")

DATA_PATH = "data/student_social_media_mental_health.csv"
OUT_DIR = "outputs"
os.makedirs(OUT_DIR, exist_ok=True)

sns.set_theme(style="whitegrid")

TARGET = "How_often_do_you_feel_depressed_or_down"
TIME_MAP = {
    "Less than an Hour": 0.5,
    "Between 1 and 2 hours": 1.5,
    "Between 2 and 3 hours": 2.5,
    "Between 3 and 4 hours": 3.5,
    "Between 4 and 5 hours": 4.5,
    "More than 5 hours": 5.5,
}


def load_and_clean():
    df = pd.read_csv(DATA_PATH)
    df = df.drop(columns=["Serial_Number", "Timestamp"], errors="ignore")
    df = df[df[TARGET].notna()].copy()

    df["Gender"] = df["Gender"].str.strip().str.lower()
    df["Gender"] = df["Gender"].map(
        lambda g: "male" if g == "male" else ("female" if g == "female" else "other")
    )

    df["UsageHoursPerDay"] = df[" What_is_the_average_time_you_spend_on_social_media_every_day"].map(
        TIME_MAP
    )

    platforms = (
        df["What_social_media_platforms_do_you_commonly_use"]
        .str.split(",")
        .explode()
        .str.strip()
        .value_counts()
        .index[:6]
        .tolist()
    )
    for p in platforms:
        df[f"Platform_{p}"] = df["What_social_media_platforms_do_you_commonly_use"].str.contains(
            p, case=False, na=False
        ).astype(int)
    df["NumPlatforms"] = df["What_social_media_platforms_do_you_commonly_use"].str.split(",").str.len()

    df = df.drop(
        columns=["What_social_media_platforms_do_you_commonly_use",
                 " What_is_the_average_time_you_spend_on_social_media_every_day"]
    )
    return df


def build_features(df):
    cat_cols = df.select_dtypes(include=["object"]).columns.tolist()
    df = pd.get_dummies(df, columns=cat_cols, drop_first=True)
    df = df.dropna()
    return df


def regression_section(X, y):
    print("=" * 70)
    print("REGRESSION: predict distress score (1-5)")
    print("=" * 70)
    models = {
        "Multiple Linear Regression": LinearRegression(),
        "Decision Tree Regressor": DecisionTreeRegressor(random_state=42),
        "Random Forest Regressor": RandomForestRegressor(random_state=42),
        "KNN Regressor": KNeighborsRegressor(),
    }
    param_grids = {
        "Multiple Linear Regression": {},
        "Decision Tree Regressor": {"model__max_depth": [3, 5, 10, None]},
        "Random Forest Regressor": {
            "model__n_estimators": [100, 300],
            "model__max_depth": [5, 10, None],
        },
        "KNN Regressor": {"model__n_neighbors": [3, 5, 7, 11]},
    }
    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    rows = []
    for name, model in models.items():
        pipe = Pipeline([("scaler", StandardScaler()), ("model", model)])
        if param_grids[name]:
            gs = GridSearchCV(pipe, param_grids[name], cv=kf, scoring="r2", n_jobs=1)
            gs.fit(X, y)
            best = gs.best_estimator_
        else:
            best = pipe
        r2 = cross_val_score(best, X, y, cv=kf, scoring="r2").mean()
        mae = -cross_val_score(best, X, y, cv=kf, scoring="neg_mean_absolute_error").mean()
        rmse = -cross_val_score(best, X, y, cv=kf, scoring="neg_root_mean_squared_error").mean()
        rows.append(
            {
                "Model": name,
                "R2": round(r2, 3),
                "MAE": round(mae, 3),
                "RMSE": round(rmse, 3),
            }
        )
        print(f"{name:28s} R2={r2:.3f}  MAE={mae:.3f}  RMSE={rmse:.3f}")
    return pd.DataFrame(rows)


def classification_section(X, y_binned):
    print()
    print("=" * 70)
    print("CLASSIFICATION: distress buckets (Low/Moderate/High)")
    print("=" * 70)
    models = {
        "Logistic Regression": LogisticRegression(max_iter=2000),
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "Random Forest": RandomForestClassifier(random_state=42),
        "KNN": KNeighborsClassifier(),
    }
    param_grids = {
        "Logistic Regression": {"model__C": [0.01, 0.1, 1, 10]},
        "Decision Tree": {"model__max_depth": [3, 5, 10, None], "model__min_samples_split": [2, 5, 10]},
        "Random Forest": {
            "model__n_estimators": [100, 300],
            "model__max_depth": [5, 10, None],
            "model__min_samples_split": [2, 5],
        },
        "KNN": {"model__n_neighbors": [3, 5, 7, 11], "model__weights": ["uniform", "distance"]},
    }
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    rows = []
    for name, model in models.items():
        pipe = Pipeline([("scaler", StandardScaler()), ("model", model)])
        gs = GridSearchCV(pipe, param_grids[name], cv=skf, scoring="f1_macro", n_jobs=1)
        gs.fit(X, y_binned)
        best = gs.best_estimator_
        acc = cross_val_score(best, X, y_binned, cv=skf, scoring="accuracy").mean()
        f1 = cross_val_score(best, X, y_binned, cv=skf, scoring="f1_macro").mean()
        prec = cross_val_score(best, X, y_binned, cv=skf, scoring="precision_macro").mean()
        rec = cross_val_score(best, X, y_binned, cv=skf, scoring="recall_macro").mean()
        rows.append(
            {
                "Model": name,
                "BestParams": str(gs.best_params_),
                "Accuracy": round(acc, 3),
                "Precision": round(prec, 3),
                "Recall": round(rec, 3),
                "F1": round(f1, 3),
            }
        )
        print(f"{name:22s} Acc={acc:.3f}  Prec={prec:.3f}  Rec={rec:.3f}  F1={f1:.3f}  | {gs.best_params_}")

    best_name = max(rows, key=lambda r: r["F1"])["Model"]
    best = models[best_name]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_binned, test_size=0.2, stratify=y_binned, random_state=42
    )
    pipe = Pipeline([("scaler", StandardScaler()), ("model", best)])
    gs = GridSearchCV(pipe, param_grids[best_name], cv=skf, scoring="f1_macro", n_jobs=1)
    gs.fit(X_train, y_train)
    y_pred = gs.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=sorted(y_binned.unique()),
                yticklabels=sorted(y_binned.unique()), ax=ax)
    ax.set_title(f"Confusion Matrix - {best_name} (Test Set)")
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    fig.tight_layout()
    fig.savefig(f"{OUT_DIR}/confusion_matrix.png", dpi=150)
    plt.close(fig)
    print(f"\nSaved confusion matrix for best model ({best_name}) to outputs/confusion_matrix.png")
    return pd.DataFrame(rows)


def clustering_section(X):
    print()
    print("=" * 70)
    print("CLUSTERING: K-Means on social media behaviour features")
    print("=" * 70)
    scaler = StandardScaler()
    Xs = scaler.fit_transform(X)
    scores = {}
    for k in range(2, 6):
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = km.fit_predict(Xs)
        scores[k] = silhouette_score(Xs, labels)
        print(f"k={k}  silhouette={scores[k]:.3f}")
    best_k = max(scores, key=scores.get)
    km = KMeans(n_clusters=best_k, random_state=42, n_init=10)
    labels = km.fit_predict(Xs)
    print(f"Best k={best_k} (silhouette={scores[best_k]:.3f})")
    return best_k, labels


def hypothesis_test(df):
    print()
    print("=" * 70)
    print("HYPOTHESIS TEST: usage hours vs distress score (Pearson r)")
    print("=" * 70)
    clean = df.dropna(subset=["UsageHoursPerDay", TARGET])
    r, p = stats.pearsonr(clean["UsageHoursPerDay"], clean[TARGET])
    print(f"r={r:.3f}, p={p:.4f}")
    print("Reject H0 (significant association)" if p < 0.05 else "Cannot reject H0")
    return r, p


def feature_importance(X, y_binned):
    print()
    print("=" * 70)
    print("FEATURE IMPORTANCE: Random Forest")
    print("=" * 70)
    rf = RandomForestClassifier(random_state=42)
    rf.fit(X, y_binned)
    imp = pd.Series(rf.feature_importances_, index=X.columns).sort_values(ascending=False)
    print(imp.head(10).round(3).to_string())
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x=imp.head(10).values, y=imp.head(10).index, ax=ax, hue=imp.head(10).index, legend=False)
    ax.set_title("Top 10 Features by Importance (Random Forest)")
    fig.tight_layout()
    fig.savefig(f"{OUT_DIR}/feature_importance.png", dpi=150)
    plt.close(fig)
    print("Saved to outputs/feature_importance.png")
    return imp


def main():
    df = load_and_clean()
    print(f"Cleaned rows: {len(df)}")

    fig, axes = plt.subplots(1, 3, figsize=(14, 4))
    sns.histplot(df[TARGET], bins=5, discrete=True, ax=axes[0])
    axes[0].set_title("Distress score distribution")
    sns.countplot(x="Gender", data=df, ax=axes[1], hue="Gender", legend=False)
    axes[1].set_title("Gender")
    sns.histplot(df["UsageHoursPerDay"].dropna(), bins=6, ax=axes[2])
    axes[2].set_title("Daily usage hours")
    fig.tight_layout()
    fig.savefig(f"{OUT_DIR}/eda_overview.png", dpi=150)
    plt.close(fig)
    print("Saved outputs/eda_overview.png")

    y = df[TARGET].astype(int)
    bins = pd.cut(y, bins=[0, 2, 3, 5], labels=["Low", "Moderate", "High"])
    y_binned = pd.Series(LabelEncoder().fit_transform(bins), index=y.index, name="DistressBucket")

    X = build_features(df.drop(columns=[TARGET]))

    r, p = hypothesis_test(pd.concat([X, df[TARGET]], axis=1))

    reg_results = regression_section(X, y)
    clf_results = classification_section(X, y_binned)
    best_k, labels = clustering_section(X)
    imp = feature_importance(X, y_binned)

    corr = pd.concat([X, y], axis=1).corr()[y.name].drop(y.name).sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(8, 8))
    sns.heatmap(pd.concat([X, y], axis=1).corr(), cmap="RdBu_r", center=0,
                annot=False, ax=ax, xticklabels=False, yticklabels=False)
    ax.set_title("Full correlation matrix")
    fig.tight_layout()
    fig.savefig(f"{OUT_DIR}/correlation_matrix.png", dpi=150)
    plt.close(fig)
    print("Saved outputs/correlation_matrix.png")

    with open(f"{OUT_DIR}/results_summary.md", "w", encoding="utf-8") as f:
        f.write("# ML Pipeline Results\n\n")
        f.write(f"Cleaned samples: {len(X)}, features: {X.shape[1]}\n\n")
        f.write(f"**H0 (usage hours vs distress): r={r:.3f}, p={p:.4f}**\n\n")
        f.write("## Regression (5-fold CV)\n")
        f.write(reg_results.to_markdown(index=False) + "\n\n")
        f.write("## Classification (5-fold CV)\n")
        f.write(clf_results.to_markdown(index=False) + "\n\n")
        f.write(f"Best K-Means k={best_k}\n\n")
        f.write("## Top 10 Features\n")
        f.write(imp.head(10).to_frame("importance").to_markdown() + "\n")
    print("\nWrote outputs/results_summary.md")


if __name__ == "__main__":
    main()
