Research complete. Compiling full report.

---

# ML DATASET + RESEARCH PAPER DISCOVERY REPORT

**Topic:** Predicting Student Mental Health from Social Media Usage

---

# 1. Project Understanding

Project proposes a supervised ML study linking social media usage patterns → student mental health outcomes. Critical framing issue found immediately:

**"Mental health score" is NOT a standardized, single scientific construct.** Published literature operationalizes mental health as:
- **Depression** — PHQ-9 (Patient Health Questionnaire) [2], CES-D [6], clinical diagnosis [9]
- **Anxiety** — GAD-7 [2]
- **Stress** — DASS-21 [2][7]
- **Psychological distress / well-being** — WEMWBS-type scales, self-report [1]
- **Risk categories** (normal/mild/moderate/severe) or binary (depressed/not) [2][7]

No peer-reviewed study predicts a single scalar "mental health score" from social media usage. Your target must be re-framed as *depression/anxiety/stress risk* or a *composite risk index* — otherwise the project has no literature basis.

**Second key finding:** The relationship is **associational, not causal**. Observational cross-sectional surveys dominate [1][6]. Even quasi-experimental designs (Facebook rollout) only establish association + plausibility, not individual causation [9]. Prediction ≠ causation — you must state this explicitly.

---

# 2. Research Question

*Can social media usage patterns (time spent, platforms, frequency, passive/active use, social comparison) predict depression/anxiety risk among students, using an open dataset and interpretable ML models?*

Re-framed from "predict mental health score" → "predict depression/anxiety risk category or composite risk score."

---

# 3. Required Variables

**Supported by literature as predictors (IVs):**
- Daily social media usage time (hours/day) [1][2][6]
- Number / type of platforms used [1][6]
- Frequency of purposeless use / distraction [1][4]
- Passive vs active consumption [5]
- Social comparison / validation seeking [5][9]
- Night-time usage [1]
- Social media addiction score (Bergen scale variants) [2][6]
- Demographics: age, gender [1][2]
- Confounders: sleep, academic pressure, financial stress, family history [2][7]

**Targets (DVs) actually used in research:**
- Depression score/risk (PHQ-9, CES-D) [2][6]
- Anxiety score/risk (GAD-7) [2]
- Stress score (DASS-21) [2][7]
- Insomnia (ISI-7) [2]

**Not assumed to exist:** a single "mental health score." It does not exist as a validated measure.

---

# 4. Literature Search Results

10+ relevant papers identified (Consensus MCP + web verification). Key themes:

1. **[1]** Osman 2025, *Scientific Reports* — University students, n=268. High SMU (>3h/day, 84.7%) strongly associated with anxiety (AOR 22.2), sleep disturbance, mental exhaustion, isolation. Private primary survey.
2. **[2]** Chowdhury et al. 2024, *Health Science Reports* — Tree-based ML (DT/RF/XGBoost) predicting anxiety/depression/insomnia in 1250 Bangladeshi students (GAD-7/PHQ-9/ISI-7). **Social media addiction was a top risk factor.** XGBoost best. Private data.
3. **[3]** Schaab et al. 2024, *Cadernos de Saúde Pública* — Systematic review: 48 studies of ML detection of depression/anxiety/stress in undergraduates. Most >70% accuracy but **47/48 internal validation only; evidence quality very low.**
4. **[4]** Phiri et al. 2025, *JMIR* — Systematic review + meta-analysis: social media **text** predicts depression (r=0.630, large effect). NLP-focused.
5. **[5]** Agyapong-Opoku et al. 2025, *Behavioral Sciences* — Scoping review of 43 reviews: association complex; problematic use + passive consumption strongest linked to harm; effects context-specific.
6. **[6]** Sujarwoto et al. 2021, *Int J Mental Health & Addiction* — 709 Indonesian students, CES-D. Higher social media addiction → higher mild-depression odds (OR 1.07).
7. **[7]** Saxena et al. 2025, *IEEE AECE* — Student depression prediction, multimodal (behavioral + linguistic), n=820, PHQ-9 ground truth, fusion ensemble 86% acc. Private dataset.
8. **[8]** Valkenburg et al. 2021, *Current Opinion in Psychology* — Umbrella review: associations mostly **"weak or inconsistent"**; mixed interpretation.
9. **[9]** Braghieri, Levy & Makarin 2022, *Nature Communications* — Facebook college rollout natural experiment; Facebook ↑ poor mental health via social comparison. **Data on ICPSR (10.3886/E175582V1).** Causal-estimation design.
10. **[10]** Feng et al. 2025, *Heliyon* — Network analysis: social media addiction ↔ anxiety/depression/stress + academic burnout, n=432 Chinese students.

---

# 5. Top 5 Highly Relevant Papers

| # | Paper | Year | Population | Social Media Variable | MH Outcome | Method | Dataset | Open Dataset? | Paper Link |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Osman, *Sci Reports* | 2025 | University students, Somalia (n=268) | Daily usage hours | Anxiety, sleep, isolation, exhaustion | Cross-sectional, logistic regression | Primary survey | No | [link](https://consensus.app/papers/details/fb6370b4e85750ceb1b67a6abc83c9cc/?utm_source=claude_desktop) |
| 2 | Chowdhury et al., *Health Sci Reports* | 2024 | Bangladeshi students (n=1250) | SM addiction, usage | Anxiety (GAD-7), Depression (PHQ-9), Insomnia (ISI-7) | DT, RF, XGBoost ML | Primary survey | No | [link](https://consensus.app/papers/details/403b3c6923635b7b961550616e79a58a/?utm_source=claude_desktop) |
| 3 | Schaab et al., *Cad Saúde Pública* | 2024 | Undergraduates (48 studies) | Various (usage, internet, behavior) | Depression/anxiety/stress | Systematic review of ML | Mixed | Mostly no | [link](https://consensus.app/papers/details/25c242d6f113506eb4c3b915392b5ab3/?utm_source=claude_desktop) |
| 4 | Phiri et al., *JMIR* | 2025 | Social media users (36 studies) | Social media text/activity | Depression | Meta-analysis (r=0.630) | Text corpora (SMHD, eRisk etc.) | Some yes | [link](https://consensus.app/papers/details/591126a4053856a29f8252e9bf5eedff/?utm_source=claude_desktop) |
| 5 | Sujarwoto et al., *IJMHA* | 2021 | Indonesian students (n=709) | SM addiction score | Depression (CES-D) | Logistic regression | Primary survey | No | [link](https://consensus.app/papers/details/9a6373ecf7285422909fc8d2b68e03ff/?utm_source=claude_desktop) |

**Partial relevance:** [9] (causal, data open but complex), [7] (ML-strong, private data), [8] (review only).

---

# 6. Paper → Dataset Mapping

| Paper | Year | Dataset | Dataset Type | Publicly Available? | Dataset URL | Target | Sample Size |
|---|---|---|---|---|---|---|---|
| Osman 2025 | 2025 | Primary survey (Mogadishu) | Primary survey | No | — | Anxiety, sleep, isolation | 268 |
| Chowdhury 2024 | 2024 | Primary survey (Bangladesh) | Primary survey | No | — | Anxiety/Depression/Insomnia | 1250 |
| Schaab 2024 | 2024 | Multiple (review) | Mixed | Mostly No | — | DAS outcomes | 48 studies |
| Phiri 2025 | 2025 | SMHD, eRisk, Dreaddit, Reddit corpora | Open text corpora | Partially | [CLPsych overview](https://aclanthology.org/2025.clpsych-1.10/) | Depression | varies |
| Sujarwoto 2021 | 2021 | Primary survey (Indonesia) | Primary survey | No | — | CES-D depression | 709 |
| Saxena 2025 | 2025 | Primary survey (n=820) | Primary survey | No | — | PHQ-9 depression | 820 |
| Braghieri 2022 | 2022 | College surveys + Facebook rollout | Secondary survey | Yes (ICPSR) | [OpenICPSR 175582](https://www.openicpsr.org/openicpsr/project/175582/version/V1/view) | Depression, wellbeing | ~14k+ (varies) |
| Explainable ML paper (Springer *Discover Mental Health*) | 2026 | **Social Media and Mental Health (Kaggle)** | Open survey | **Yes** | [Kaggle](https://www.kaggle.com/datasets/souvikahmed071/social-media-and-mental-health) | Depression/anxiety risk (composite) | 481 |

**Key pattern:** The studies most directly matching your topic (student + social media usage → MH) all used **private primary survey data**. Only the Kaggle survey dataset is both on-topic **and** open. This is the reproducibility gap you can exploit.

---

# 7. Open Dataset Investigation

Verified sources (Playwright/UCI API/web; all links checked live):

1. **Social Media and Mental Health** — Kaggle `souvikahmed071/social-media-and-mental-health` — **VERIFIED**: 481 rows, 21 columns, ODbL license, 61% university students, age 13–91, survey Apr–Nov 2022. Used by a published Springer paper (SHAP/LIME nested CV). [Official](https://www.kaggle.com/datasets/souvikahmed071/social-media-and-mental-health)
2. **Student Mental health (100-row)** — Kaggle `shariful07/student-mental-health` — **VERIFIED**: 101 rows, 11 cols, CC0 Public Domain, IIUM Malaysia survey. Depression (16 yes), Anxiety (35), Panic (34), Treatment (33). [Official](https://www.kaggle.com/datasets/shariful07/student-mental-health) | UCI mirror page blocked (403) — "Not verified" at UCI.
3. **Student Depression Dataset** — Kaggle `hopesb/student-depression-dataset` — **VERIFIED**: 27,902 rows, 18 cols, Indian students K12–PhD. **IMPORTANT: synthetic data** (stated in Frontiers 2026 paper + multiple sources). No social media variables. [Official](https://www.kaggle.com/datasets/hopesb/student-depression-dataset)
4. **PHQ-9 Student Depression Dataset** — Mendeley, DOI **10.17632/kkzjk253cy.6** — **VERIFIED**: 682 students, CC BY 4.0, clinically supervised, PHQ-9 severity scores. No social media vars. [Official](https://data.mendeley.com/datasets/kkzjk253cy/6)
5. **Student_mental_health_related_records** — Mendeley, DOI **10.17632/hy4653fg79.1** — **VERIFIED**: 400 students, Bangladesh, depression/anxiety/panic/treatment binaries. [Official](https://data.mendeley.com/datasets/hy4653fg79/1)
6. **Social Media & Mental Health (US students)** — BSOS UMD repository — **VERIFIED as listing**: ODC-PDDL, PHQ-9/GAD-7, US students. **Content of social-media variables NOT verified** — teaching repository, proceed cautiously. [Official](https://bsos-data.umd.edu/dataset/social-media-and-mental-health) | Source DOI 10.3886/E175582V1
7. **Survey Dataset on Students' Social Media Usage, Addiction...** — IEEE DataPort, DOI **10.21227/kx3c-1043** — **VERIFIED**: exactly on-topic variables (Avg_Daily_Usage_Hours, Most_Used_Platform, Mental_Health_Score, Addicted_Score) but **subscription required — NOT free**. [Official](https://ieee-dataport.org/documents/survey-dataset-students-social-media-usage-addiction-severity-sleep-mental-well-being-and)
8. **Student Stress Factors** — Kaggle, 1,100 rows, 21 cols (stress). Used by 2025 stress-ML paper [arXiv 2508.01105](https://arxiv.org/html/2508.01105v1). No social media vars.

---

# 8. Top 10 Candidate Datasets

| Rank | Dataset | Rows | Features | Target | Open? | Paper Support | ML Suitability | Research Suitability | Score /10 |
|---|---|---|---|---|---|---|---|---:|---:|
| 1 | Student Depression Dataset (Kaggle hopesb) | 27,902 | 18 | Depression (binary) | Yes | High (Frontiers 2026 + others) | High | **Low (synthetic)** | 7.2 |
| 2 | **Social Media & Mental Health (Kaggle souvikahmed071)** | 481 | 21 | Depression/anxiety composite | Yes (ODbL) | Medium (Springer 2026) | Medium | **High (real, on-topic)** | 7.05 |
| 3 | PHQ-9 Student Depression (Mendeley) | 682 | ~30 | PHQ-9 score/severity | Yes (CC BY 4.0) | Low | High | Medium | 6.85 |
| 4 | SM Usage/Addiction Survey (IEEE DataPort) | unknown | 12+ | MH score + addiction score | **No (subscription)** | None | Medium | High (on-topic) | 6.8 |
| 5 | SM & MH US students (BSOS UMD) | unknown | unknown | PHQ-9/GAD-7 | Yes (PDDL) | Medium (Braghieri) | Medium | Medium (unverified) | 6.2 |
| 6 | Student Mental health 100-row (Kaggle/UCI) | 101 | 11 | Depression/Anxiety/Panic | Yes (CC0) | Low | Low | Medium | 5.6 |
| 7 | Student Stress Factors (Kaggle) | 1,100 | 21 | Stress | Yes | Medium (2025 paper) | Medium | Low (no SM vars) | 5.5 |
| 8 | Mental Health in Tech (Kaggle OSMI) | 1,259 | 27 | MH conditions | Yes | High | Medium | **Low (not students, no SM)** | 5.5 |
| 9 | Anxiety & Depression MH Factors (Kaggle) | ~1,000 | 20+ | Anxiety/Depression | Yes | Medium | Medium | Low | 5.4 |
| 10 | Student_mental_health_related_records (Mendeley) | 400 | 12 | Depression/Anxiety/Panic | Yes (CC BY) | Low | Low | Medium | 5.15 |

---

# 9. Dataset Comparison

- **Only on-topic + open + real-survey:** the **481-row Kaggle "Social Media and Mental Health"**. Every other open student-MH dataset lacks social-media usage variables.
- **Biggest + most ML-friendly:** hopesb Student Depression (27.9k rows) but **synthetic** → weak research validity, and no SM variables.
- **Best clinically-validated target:** Mendeley PHQ-9 (real clinical scale) but no SM features.
- **Best on-topic variables:** IEEE DataPort, but paywalled.
- **Leakage check:** In the 481-row set, no feature is measured after the outcome (single cross-sectional survey). In hopesb, "Suicidal Thoughts" is near-identical to the outcome construct (target leakage risk) — see [Frontiers pipeline analysis](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1864665/full).
- **Bias checks:** 481-row set = convenience/self-report, age 13–91 skew, 61% students (not pure-student). hopesb = India-only, K12–PhD, synthetic. Both single-country/region.

---

# 10. Top 3 Dataset Recommendations

### Dataset A — **Social Media and Mental Health** (Kaggle, souvikahmed071) — *best topical fit*
- **Why it fits:** only open dataset with real SMU predictors + MH outcomes + student majority; has published-paper precedent (Springer SHAP/LIME study).
- **Features (21):** age, gender, relationship status, occupation, platforms used, avg daily time, purposeless-use frequency, distraction frequency, restlessness, comparison frequency, validation seeking, worry, "feels depressed" scale, productivity impact, etc.
- **Target:** engineer composite **Depression** and **Anxiety** risk indicators from the 1–5 scale items (as the published study did).
- **ML problem:** classification (risk yes/no) + optional regression on composite score.
- **Models:** Logistic Regression, Decision Tree, Random Forest, KNN. Avoid deep models — 481 rows.
- **Advantages:** on-topic, free ODbL, real survey, paper support.
- **Limitations:** small n, self-report bias, no validated clinical scale, age range includes non-students.
- **Ethics:** self-report sensitive data, anonymized; no clinical claims.
- **Reproducibility:** yes — free Kaggle download.

### Dataset B — **Student Depression Dataset** (Kaggle, hopesb) — *best ML-learning value*
- 27,902 rows, 18 cols, binary Depression target. DT/RF/XGBoost achieve high accuracy; huge community + paper support.
- **Critical caveat: synthetic data** — fine for ML practice, weak for "research methodology" claims. No SM variables.
- **Reproducibility:** yes.

### Dataset C — **PHQ-9 Student Depression** (Mendeley) — *best target validity*
- 682 students, clinically supervised, PHQ-9 severity (validated). Great target + multi-class option.
- No social media features → would need to re-frame research question toward "demographic/academic → depression."
- **Reproducibility:** yes, CC BY 4.0.

---

# 11. Best Dataset

## BEST DATASET
**Name:** Social Media and Mental Health
**Official Dataset Link:** https://www.kaggle.com/datasets/souvikahmed071/social-media-and-mental-health
**Dataset Source:** Primary online survey (Apr–Nov 2022), created for a university Statistics project; hosted on Kaggle
**License:** ODbL — Open Database License (Database: Open Database, Contents: © Original Authors)
**Rows:** 481
**Columns:** 21
**Target:** Composite depression/anxiety risk indicators (engineered from 1–5 scale items; no single validated "mental health score")
**Main Features:** age, gender, relationship status, occupation, organizations, platforms used, average daily time, purposeless use, distraction, restlessness, worry, social comparison, validation seeking, depressed-feeling frequency, productivity impact
**ML Task:** Classification (binary risk: depressed/anxious vs not) — optionally regression on composite score
**Recommended Models:** Logistic Regression, Decision Tree, Random Forest, KNN
**Recommended Evaluation Metrics:** Accuracy, Precision, Recall, F1, Confusion Matrix, ROC-AUC (classification); MAE/RMSE/R² (if regression)
**Research Papers Supporting Its Use:** Springer *Discover Mental Health* "Explainable ML for mental health prediction from social media behavior" (SHAP/LIME, nested CV); plus the method family in [1][2][4]
**Open/Publicly Available:** Yes (ODbL, free download)
**Research Suitability Score:** 7.5/10
**ML Suitability Score:** 7.0/10
**Overall Score:** 7.05/10

---

# 12. Research Gap

**Defensible gap (supported by literature):**
- Almost all student + social-media-usage → mental-health studies used **private, non-reproducible survey data** [1][2][6][7].
- ML reviews find most student-MH models used **internal validation only** (47/48 studies) with very low evidence quality [3].
- Only **one open, on-topic dataset** (481-row Kaggle) exists, and it is **small and without validated clinical scales**; the large alternative (27.9k) is **synthetic**.
- Structured usage-behavior features (vs NLP text) are underrepresented relative to text-based depression detection [4].

→ **Gap: reproducible, interpretable benchmarking of social-media-usage → student depression/anxiety-risk prediction on an open dataset, with honest external/internal validation and feature-importance analysis.** Your project fits this gap naturally.

If you judge the evidence too thin for that framing, the fallback statement: *"No defensible research gap established beyond the reproducibility limitation."* But the reproducibility gap is real and paper-supported.

---

# 13. Proposed Research Problem

Social media usage is strongly associated with depression/anxiety among students [1][2][6], yet most studies use private datasets and unvalidated models [3]. It is unclear whether structured social-media-usage indicators alone can predict student depression/anxiety risk on an open, reproducible dataset, and which features matter most.

---

# 14. Research Objectives
1. Preprocess and clean the open 481-row social-media/mental-health dataset (missingness, encoding, scaling).
2. Engineer composite depression/anxiety risk targets from survey items.
3. Train interpretable classifiers (Logistic Regression, Decision Tree, Random Forest, KNN).
4. Compare models via cross-validation; report accuracy, precision, recall, F1, ROC-AUC.
5. Identify top predictive features via feature importance / SHAP.
6. State association-vs-causation limits explicitly.

---

# 15. Research Questions
1. Do structured social-media usage indicators predict depression/anxiety risk in the open survey dataset?
2. Which usage indicators (time, platforms, passive use, comparison, validation-seeking) are strongest predictors?
3. Which interpretable ML model performs best on this small dataset without overfitting?

---

# 16. Hypotheses
- **H0:** Social-media usage indicators have no statistically significant association with depression/anxiety risk score.
- **H1:** At least one social-media usage indicator is significantly associated with depression/anxiety risk score (e.g., logistic-regression coefficient ≠ 0 at α=0.05).

*(Testable via logistic regression; do not claim causation.)*

---

# 17. Proposed ML Pipeline
Dataset (Kaggle 481-row) → Data Understanding → Data Cleaning → Missing-value handling → Duplicate removal → EDA + visualizations → Feature engineering (composite targets, encode platforms) → Encoding (one-hot/label) → Scaling → Feature selection (correlation/importance) → Train/Test split (stratified) → Model training (LR, DT, RF, KNN) → Cross-validation (k-fold) → Model comparison → Evaluation (metrics above) → Interpretation (feature importance) → Conclusion

---

# 18. Recommended Algorithms
- **Classification:** Logistic Regression, Decision Tree, Random Forest, KNN (matches your coursework; no deep learning — 481 rows).
- Optional: Naive Bayes for baseline.
- Do NOT add gradient boosting/neural nets — unjustified at this n.

---

# 19. Evaluation Metrics
- **Classification:** Accuracy, Precision, Recall, F1, Confusion Matrix, ROC-AUC.
- **Optional regression (composite score):** MAE, MSE, RMSE, R².
- Cross-validation accuracy to diagnose over/underfitting.

---

# 20. Ethical Considerations
- Sensitive self-reported mental-health data; dataset is anonymized — do not attempt re-identification.
- Respect ODbL attribution requirements.
- **Do not claim the model is a diagnostic system.** It is a correlation-based academic exercise [1][3][8].
- Report self-report bias, convenience sampling, cross-sectional limits.
- Avoid stigmatizing framing ("social media addicts") — use neutral language.
- Model performance does not imply a student is "at risk" clinically; no deployment.

---

# 21. Limitations
- n=481 → weak statistical power, overfitting risk.
- No validated clinical scale (composite targets are self-engineered).
- Cross-sectional → association only, no causality [1][5][8].
- 61% students → not a pure student population; mixed age range.
- Self-report/social-desirability bias.
- Single dataset, single language → weak external validity [3].
- Alternative large dataset (hopesb) is synthetic — cannot substitute.

---

# 22. Final Recommendation

Adopt the **481-row Social Media and Mental Health dataset** as primary. It is the only open, real-survey dataset with social-media-usage predictors + mental-health outcomes and published-paper precedent. If the methodology component needs a larger, cleaner ML playground, you may run a *secondary comparison* on the synthetic 27.9k Student Depression Dataset — but clearly label it synthetic and do not base research claims on it.

---

## Recommended Dataset

**Dataset:** Social Media and Mental Health (Kaggle)
**Official Link:** https://www.kaggle.com/datasets/souvikahmed071/social-media-and-mental-health
**Open/Public:** Yes — ODbL, free download, 481 rows × 21 cols
**Target Variable:** Composite depression/anxiety risk indicator (engineered; no single validated "mental health score" exists in the literature — re-frame title to "depression/anxiety risk")
**ML Task:** Binary classification (risk vs not) — optional regression on composite score
**Best 3 Models:** Logistic Regression, Decision Tree, Random Forest (KNN baseline optional)
**Best Evaluation Metrics:** Accuracy, Precision, Recall, F1, Confusion Matrix, ROC-AUC (+ MAE/RMSE/R² if regression)
**Relevant Published Papers:** Springer *Discover Mental Health* (SHAP/LIME, 481-row set); Osman 2025 [1]; Chowdhury 2024 [2]; Schaab 2024 [3]; Phiri 2025 [4]; Sujarwoto 2021 [6]
**Research Gap:** Reproducible, validated benchmarking of social-media-usage → student depression/anxiety prediction on open data (prior studies: private data [1][2][6], internal-only validation [3])
**Main Limitation:** Small sample (n=481), self-report, composite non-clinical target, cross-sectional (association ≠ causation)
**Overall Score: 7.05/10**
**Verdict: USE WITH CAUTION**

---

**Papers cited:**
[1] [Social media use and associated mental health indicators among University students: a cross-sectional study](https://consensus.app/papers/details/fb6370b4e85750ceb1b67a6abc83c9cc/?utm_source=claude_desktop) (Osman, 2025, Scientific Reports)
[2] [Predicting anxiety, depression, and insomnia among Bangladeshi university students using tree-based machine learning models](https://consensus.app/papers/details/403b3c6923635b7b961550616e79a58a/?utm_source=claude_desktop) (Chowdhury et al., 2024, Health Science Reports)
[3] [How do machine learning models perform in the detection of depression, anxiety, and stress among undergraduate students? A systematic review](https://consensus.app/papers/details/25c242d6f113506eb4c3b915392b5ab3/?utm_source=claude_desktop) (Schaab et al., 2024, Cadernos de Saúde Pública)
[4] [Text-Based Depression Prediction on Social Media Using Machine Learning: Systematic Review and Meta-Analysis](https://consensus.app/papers/details/591126a4053856a29f8252e9bf5eedff/?utm_source=claude_desktop) (Phiri et al., 2025, Journal of Medical Internet Research)
[5] [Effects of Social Media Use on Youth and Adolescent Mental Health: A Scoping Review of Reviews](https://consensus.app/papers/details/cc4b27ab8802584abca464c7e239b797/?utm_source=claude_desktop) (Agyapong-Opoku et al., 2025, Behavioral Sciences)
[6] [Social Media Addiction and Mental Health Among University Students During the COVID-19 Pandemic in Indonesia](https://consensus.app/papers/details/9a6373ecf7285422909fc8d2b68e03ff/?utm_source=claude_desktop) (Sujarwoto et al., 2021, International Journal of Mental Health and Addiction)
[7] [Student Depression Prediction: A Multimodal Machine Learning Approach](https://consensus.app/papers/details/86cf040752d7510b93019efa122bb596/?utm_source=claude_desktop) (Saxena et al., 2025, IEEE AECE)
[8] [Social media use and its impact on adolescent mental health: An umbrella review of the evidence](https://consensus.app/papers/details/fdac706f34865008897b154ea3602095/?utm_source=claude_desktop) (Valkenburg et al., 2021, Current Opinion in Psychology)
[9] [Data and Code for: Social Media and Mental Health (Facebook natural experiment)](https://www.openicpsr.org/openicpsr/project/175582/version/V1/view) (Braghieri, Levy & Makarin, ICPSR 175582)
[10] [The relationships between mental health and social media addiction... Chinese college students](https://consensus.app/papers/details/506f0cce212d5cf096e58feebca5d99d/?utm_source=claude_desktop) (Feng et al., 2025, Heliyon)

Upgrade to Consensus Pro to return 20 results per search instead of 10, and include more data like study design and key takeaways for every result.: https://consensus.app/pricing/?utm_source=claude_desktop