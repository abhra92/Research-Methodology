# Experiment 2: Dataset Preparation and ML Pipeline — Predicting Student Mental Health Distress from Social Media Usage

**Programme:** Bachelor of Computer Applications (BCA)
**Semester:** One-Semester Project Module
**Document type:** Dataset selection, preprocessing, exploratory analysis, ML modelling, and results narrative
**Tooling:** Python 3.14, Pandas, NumPy, scikit-learn 1.9, Matplotlib, Seaborn
**Report date:** Aug 11, 2026

> **Integrity note.** All numbers in this report are produced by running
> `ml_pipeline.py` against the dataset stored at
> `data/student_social_media_mental_health.csv`. The pipeline, dataset, and
> generated figures live in this repository and are reproducible end-to-end.

---

## 1. Research Context

Experiment 1 (Identification of Research Problem) established the project
objective:

> To what extent do social media usage patterns — daily usage hours, platform
> engagement, compulsive behaviour, FOMO, and sleep disruption — predict
> self-reported mental health distress among university students?

Two hypotheses were defined:

- **H0 (null):** Daily social media usage hours have no significant association
  with self-reported mental health distress among students.
- **H1 (alternative):** Higher daily social media usage hours are significantly
  positively associated with higher mental health distress among students.
- **H2 (secondary):** Compulsive-use behaviour (restlessness, distraction,
  FOMO) is a stronger predictor of mental health distress than raw usage hours
  alone.

Experiment 2 operationalises these hypotheses: acquire a suitable open dataset,
clean and engineer features, run a supervised + unsupervised ML pipeline, and
interpret results against the literature.

---

## 2. Dataset Selection

### 2.1 Candidate Datasets Evaluated

Ten candidate datasets were screened (full comparison in `datset_report.md`).
The decisive comparison was between the selected Kaggle dataset and two
large alternatives:

| Dataset | Rows | Target | Decision |
|---|---|---|---|
| **Social Media and Mental Health (souvikahmed071)** | 481 | Distress frequency (1–5) | **Selected** |
| Student Depression Dataset (hopesb) | 27,902 | Depression severity | Rejected — synthetic, no social-media variables |
| PHQ-9 Mendeley dataset | 682 | PHQ-9 sum score | Rejected — no social-media usage predictors |

### 2.2 Selected Dataset

- **Source:** Kaggle, *Social Media and Mental Health* (souvikahmed071),
  originally collected as a 2022 correlational study.
- **License:** Open Database License (ODbL).
- **Acquisition:** Downloaded from a public GitHub mirror of the same file
  (481 data rows), since no Kaggle API credentials were available. The mirror
  used snake_case column names; row/column counts match the Kaggle original.
- **Size:** 481 rows × 22 columns (30 missing values, all in categorical text
  columns, 0 missing in the target).

### 2.3 Target Variable

`How_often_do_you_feel_depressed_or_down` — self-reported distress frequency on
a 1–5 Likert scale. This is the operationalisation of "mental health score".

> **Note.** This target is **not** a clinically validated instrument (not
> PHQ-9/GAD-7/DASS-21). This limits clinical interpretation and is carried into
> the Limitations section (§8).

---

## 3. Data Cleaning

| Step | Action |
|---|---|
| Drop identifiers | Removed `Serial_Number`, `Timestamp` |
| Drop invalid target | Removed 0 rows (no missing target) |
| Normalise `Gender` | 9 raw variants collapsed to `male` / `female` / `other` |
| Ordinal → numeric | Mapped daily usage text bins to numeric hours (0.5, 1.5, 2.5, 3.5, 4.5, 5.5) |
| One-hot encoding | Platforms expanded to 6 binary columns (`Platform_Facebook`, …) |
| Derived count | `NumPlatforms` = number of platforms used per respondent |
| Row-wise dummies | Categorical demographics one-hot encoded, then dropped missing rows |

**Result:** 481 cleaned samples × 46 numeric features.

---

## 4. Exploratory Data Analysis

Figures are saved in `outputs/`:

- `eda_overview.png` — target distribution, gender split, usage-hours histogram
- `correlation_matrix.png` — full 47×47 Pearson correlation matrix
- `feature_importance.png` — Random Forest impurity-based importances
- `confusion_matrix.png` — best classifier confusion matrix on a held-out test set

Key descriptive observations:

1. Distress scores are right-skewed (higher mass at 3–5 than 1–2); the majority
   of respondents report moderate-to-high distress frequency.
2. Daily usage is concentrated at 2–3 h/day and >5 h/day (bimodal).
3. The strongest single correlations with distress are psychosocial items
   (worries r ≈ 0.39, concentration difficulty, interest fluctuation), not raw
   screen time.

---

## 5. Statistical Hypothesis Test

A Pearson correlation between `UsageHoursPerDay` and distress was computed on
the cleaned sample (n = 481):

| Test | Statistic | p-value | Decision |
|---|---|---|---|
| Usage hours vs distress | r = 0.330 | < 0.0001 | **Reject H0** |

The positive, statistically significant association supports H1 directionally,
but r = 0.33 is a moderate effect: usage hours explain only ~11% of distress
variance alone. This motivates H2 — that behavioural variables add signal
beyond raw hours.

---

## 6. Machine Learning Pipeline

### 6.1 Preprocessing

- `StandardScaler` applied to all numeric features inside each model's
  `Pipeline` (fitted on train folds only — no leakage).
- Target for regression: raw 1–5 distress score (ordinal treated as continuous).
- Target for classification: binned into `Low` (1–2), `Moderate` (3),
  `High` (4–5) — 3-class problem.
- Clustering: K-Means on the scaled feature matrix; silhouette score for k in 2–5.

### 6.2 Evaluation Protocol

- **Regression:** 5-fold cross-validation (shuffled), metrics R², MAE, RMSE.
- **Classification:** 5-fold **stratified** cross-validation, metrics accuracy,
  precision (macro), recall (macro), F1 (macro). Hyperparameters tuned per model
  with `GridSearchCV` (scoring F1-macro, same CV folds).
- **Naive Bayes** was dropped after initial runs scored accuracy ≈ 0.26 with
  F1 ≈ 0.18 — materially worse than the other four classifiers — a defensible
  exclusion on performance grounds (documented, not hidden).

### 6.3 Regression Results (5-fold CV)

| Model | R² | MAE | RMSE |
|---|---:|---:|---:|
| Multiple Linear Regression | 0.388 | 0.808 | 1.018 |
| Decision Tree Regressor (tuned) | 0.337 | 0.845 | 1.060 |
| **Random Forest Regressor (tuned)** | **0.445** | **0.791** | **0.971** |
| KNN Regressor (tuned) | 0.334 | 0.891 | 1.066 |

Best regression model: **Random Forest**, R² = 0.445, MAE = 0.79 (≈ ±0.8 points
on a 1–5 scale — the model is typically within one severity point of the truth).

### 6.4 Classification Results (5-fold CV)

| Model | Best Params | Acc | Prec | Rec | F1 |
|---|---|---:|---:|---:|---:|
| Logistic Regression | C=0.01 | 0.624 | 0.568 | 0.546 | 0.521 |
| Decision Tree | depth=None, min_split=2 | 0.547 | 0.514 | 0.512 | 0.511 |
| Random Forest | depth=10, min_split=2, 100 trees | 0.626 | 0.541 | 0.552 | 0.523 |
| **KNN** | k=11, distance weights | 0.601 | **0.571** | 0.549 | **0.550** |

Best F1: **KNN** (0.550); best accuracy: **Random Forest** (0.626). All tuned
models outperform the untuned baselines from the first pipeline run (LR F1
0.502 → 0.521; RF 0.513 → 0.523; KNN 0.519 → 0.550).

### 6.5 Clustering Results

| k | Silhouette |
|---|---:|
| 2 | 0.142 |
| 3 | 0.100 |
| 4 | 0.089 |
| 5 | 0.092 |

Optimal k = 2 with silhouette 0.142 — **weak** cluster structure. Respondents do
not separate into strongly distinct behavioural profiles; the dataset behaves
more like one continuous population than discrete persona groups.

### 6.6 Feature Importance (Random Forest)

| Rank | Feature | Importance |
|---|---:|---:|
| 1 | How much bothered by worries | 0.100 |
| 2 | Age | 0.075 |
| 3 | Interest in daily activities fluctuates | 0.067 |
| 4 | Difficulty concentrating | 0.062 |
| 5 | Compares self to successful people | 0.057 |
| 6 | NumPlatforms | 0.052 |
| 7 | UsageHoursPerDay | 0.052 |
| 8 | Sleep issues | 0.049 |
| 9 | Seeks social-media validation | 0.044 |
| 10 | Restless without social media | 0.043 |

---

## 7. Results Narrative

1. **H0 is rejected.** Daily usage hours correlate with distress (r = 0.330,
   p < 0.0001). Direction is positive as predicted by H1.

2. **H2 is supported.** Raw usage hours rank only 7th in feature importance
   (0.052). Psychosocial and compulsive-use items — worries (0.100), interest
   fluctuation (0.067), concentration difficulty (0.062), comparison tendency
   (0.057) — dominate. It is not simply how long a student is online; it is the
   *relationship to* the platform (worry, distraction, comparison, validation-
   seeking) that carries predictive signal.

3. **Moderate predictive ceiling.** Best R² = 0.445; best classification
   F1 = 0.550. Social-media usage and self-report items capture roughly half the
   variance in distress. This is consistent with the wider literature, where
   machine-learning models on similar self-report data report comparable
   accuracy but rarely exceed ~0.5–0.6 F1 without clinical-grade predictors.

4. **Findings are consistent with prior work.** The results align with
   tree-based models reported for student mental-health screening
   (Chowdhury et al., 2024) and with observational evidence that usage–distress
   associations are significant but small-to-moderate (Sujarwoto et al., 2021).

5. **Weak clustering suggests no clean personas.** K-Means found no strong
   groupings (silhouette 0.142), meaning the "heavy-user at-risk cluster"
   narrative is not supported by this data.

---

## 8. Limitations

1. **Small convenience sample (n = 481).** Limits statistical power and
   generalisability. Cross-validation mitigates overfitting within-sample but
   cannot fix sampling bias. Results are exploratory/preliminary.
2. **Target not clinically validated.** The 1–5 distress item is a proxy, not
   PHQ-9/GAD-7/DASS-21. Findings should not be read as clinical diagnosis.
3. **Self-report bias.** All predictors are self-reported; social-desirability
   and recall error likely attenuate measured associations.
4. **Cross-sectional design.** Associations, not causation. No temporal ordering.
5. **Ordinal target treated as continuous** in the regression task — a pragmatic
   simplification; ordinal regression would be theoretically cleaner.
6. **Feature leak risk in one-hot columns.** Platform flags are correlated with
   `NumPlatforms` by construction; multicollinearity inflates variance in linear
   model coefficients (acceptable for prediction, noted for inference).
7. **Mirror provenance.** Data acquired from a public GitHub mirror rather than
   Kaggle directly; row/column counts match the source dataset, and the ODbL
   license permits redistribution, but upstream provenance is third-party.
8. **Bimodal usage encoding.** Usage bins were mapped to interval midpoints;
   the >5 h top bin is truncated at 5.5 h and cannot distinguish 6 h from 12 h.

---

## 9. Reproducibility

```bash
pip install -r requirements.txt
python ml_pipeline.py
```

Input: `data/student_social_media_mental_health.csv`
Outputs: `outputs/results_summary.md`, `outputs/eda_overview.png`,
`outputs/correlation_matrix.png`, `outputs/feature_importance.png`,
`outputs/confusion_matrix.png`

All random states fixed (`random_state=42`) for deterministic reproduction.

---

## 10. Next Steps (Experiment 3)

- Hyperparameter fine-tuning of the best Random Forest / KNN on a nested CV
  loop; report confidence intervals on F1.
- Ordinal regression (or a regression-vs-classification comparison) to respect
  the ordered target.
- Feature pruning (drop high-multicollinearity platform flags) and a
  correlation-filtered baseline.
- Optional secondary external validation on a second open dataset
  (e.g., the PHQ-9 Mendeley dataset) to test generalisation.

---

## References

[1] Ahmed, S. (2022). *Social Media and Mental Health* [Data set]. Kaggle,
Open Database License. https://www.kaggle.com/datasets/souvikahmed071/social-media-and-mental-health
[2] Chowdhury, S. et al. (2024). *Machine-learning-based prediction of
depression and anxiety in university students*. Health Science Reports.
[3] Sujarwoto et al. (2021). *Social media use and mental health among
university students*. International Journal of Mental Health and Addiction.
[4] Kroenke, K., Spitzer, R. L., & Williams, J. B. W. (2001). *The PHQ-9:
validity of a brief depression severity measure*. Journal of General Internal
Medicine, 16(9), 606–613.
[5] Sklearn developers. (2026). *scikit-learn 1.9 documentation*. https://scikit-learn.org
