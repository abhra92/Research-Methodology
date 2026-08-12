# Systematic Literature Review (SLR): Generative AI
## Discovering an Original Research Problem — 2026 Publications, Sorted by Citation Count

**Prepared as:** Research Methodology (7th Sem BCA) — SLR exercise
**Search date:** 7 August 2026
**Corpus size:** 30 papers (2026 publications)
**Sorting:** Google Scholar "Cited by" (descending), cross-validated with OpenAlex

---

## 1. SLR Protocol (PRISMA-style)

| Item | Description |
|---|---|
| **Research domain** | Generative AI (GenAI) |
| **Databases searched** | Google Scholar ✅ (30 results extracted), Springer Link ✅, IEEE Xplore ⚠️ (bot-wall, results not machine-readable), ACM Digital Library ⚠️ (HTTP 403) |
| **Supplementary sources** | OpenAlex API, Semantic Scholar API, Crossref API (used to verify metadata + retrieve abstracts for paywalled papers) |
| **Tooling** | Playwright (headless Chromium) scraper + REST API harvesters (scripts & raw data in `.slr/`) |
| **Search string** | `"generative AI"`, filtered `since 2026` |
| **Inclusion criteria** | (a) Published/issued in 2026 (journal issue year or first-release); (b) topic = Generative AI; (c) English; (d) peer-reviewed journal/conference or high-impact working paper series |
| **Exclusion criteria** | Pre-2026-only versions, non-scholarly items, duplicates across databases |
| **Screening** | 43,200 Scholar hits → top 30 (by relevance × 2026 filter) screened → 30 included; ranked by Scholar citation count |
| **Citation note** | Scholar counts include citing preprints (higher); OpenAlex counts journal version only (lower). Both shown. |

### Corpus Overview (all 30 papers, sorted by Scholar citations)

| # | Paper (short name) | Venue (2026) | Scholar cites | OpenAlex cites |
|---|---|---|---|---|
| 1 | Bick et al. — The Rapid Adoption of Generative AI | Management Science / NBER WP 32966 | 665 | 94 |
| 2 | Cools & Diakopoulos — GenAI in the Newsroom | Journalism Practice 20(3) | 300 | 145 |
| 3 | Sedkaoui & Benaichouba — GenAI as Transformative Force | European J. of Innovation Mgmt 29(3) | 218 | 120 |
| 4 | Liu & Wang — Who on Earth Is Using GenAI? | World Development / World Bank WP | 163 | 48 |
| 5 | Lee et al. — GenAI in the Language Classroom | Interactive Learning Environments | 158 | 94 |
| 6 | Cheng et al. — GenAI for Requirements Engineering | Software: Practice & Experience | 136 | 26 |
| 7 | Kim et al. — Student–GenAI Interaction Patterns | J. of Computing in Higher Education | 106 | 45 |
| 8 | Pallant et al. — GenAI & Student Learning Outcomes | Studies in Higher Education | 105 | 49 |
| 9 | Park & Nan — GenAI and Misinformation | AI & Society | 70 | 33 |
| 10 | Mohammadi et al. — GenAI in Academic Practices (20 countries) | Information Processing & Management | 60 | 30 |
| 11 | Daniotti et al. — Who Is Using AI to Code? | Science 391(6787) | 55 | 8 |
| 12 | Zhou et al. — GenAI in Industrial Machine Vision | J. of Intelligent Manufacturing 37 | 52 | 28 |
| 13 | Uddin et al. — Critical Analysis of GenAI | Archives of Computational Methods in Eng. 33 | 50 | 19 |
| 14 | Mohamed & Aljuaid — Historical Context as Trust Anchor | Information and Software Technology | 48 | 0 |
| 15 | Heitmann et al. — Visual GenAI in Marketing | Journal of Marketing | 33 | 13 |
| 16 | Yu et al. — GenAI Adoption in Chinese Business Schools | Int. J. of Management Education | 28 | 16 |
| 17 | Podder et al. — Green Prompt Engineering | Environmental Science & Ecotechnology | 20 | 0 |
| 18 | Brezovec et al. — Truth in Educational Sciences | Kybernetes 55(13) | 17 | 4 |
| 19 | Guo et al. — GenAI & Supply Chain Resilience | Technological Forecasting & Social Change | 16 | 10 |
| 20 | Sui & Chang — Generative AI and Education | Educational Technology & Society | 15 | – |
| 21 | Singu et al. — Responsible AI for Trustworthy Tourism | Technological Forecasting & Social Change | 13 | 10 |
| 22 | Madzík et al. — ChatGPT in Science and Research | J. of Innovation & Knowledge | 13 | 4 |
| 23 | Liang et al. — GenAI in Education (HAI perspective) | British J. of Educational Technology | 12 | 2 |
| 24 | Te'eni et al. — CORE-Sandbox Experiments | Int. J. of Information Management | 12 | 2 |
| 25 | Rahiem — GenAI in Indonesian Higher Education | Social Sciences & Humanities Open | 10 | 1 |
| 26 | Rismanchian et al. — What Undergrads Know About GenAI | Computers & Education: AI | 8 | 1 |
| 27 | Tac & Kuhl — GenAI for Material Design | Computer Methods in Applied Mechanics & Eng. | 6 | 2 |
| 28 | Jia et al. — Bias in GenAI Travel Planners | Tourism Management | 3 | 3 |
| 29 | Zheng et al. — GenAI in Healthcare | J. of Management Analytics | 3 | 0 |
| 30 | Montefiore et al. — GenAI & Meaningful Creative Work | Journal of Business Ethics | 3 | 1 |

---


## 2. Paper-by-Paper Extraction (Top 12 by citations)

> Fields marked * are inferred from the title/venue/snippet where the abstract was paywalled; all other fields are extracted from verified abstracts (OpenAlex/Crossref/publisher pages).

### P1. Bick, Blandin & Deming (2026) — *The Rapid Adoption of Generative AI* — Management Science — 665 cites
- **Objective:** Measure the speed and intensity of GenAI adoption in the U.S. and compare it with historical technologies (PC, Internet).
- **RQ:** How fast is GenAI diffusing, who adopts it, and for what tasks (work vs. home)?
- **Methodology:** Nationally representative survey (Real-Time Population Survey waves), benchmarked against CPS historical adoption series; descriptive + regression analysis.
- **Dataset:** U.S. adults aged 18–64 (survey waves 2024); historical CPS data.
- **Results:** ~39% of U.S. adults used GenAI within ~2 years of launch; ~1 in 4 employed workers used it for work in the reference week — adoption **faster than the PC and the Internet**; usage skews young, educated, male, STEM/managerial.
- **Limitations:** U.S.-only; self-reported use; snapshot in time; no direct productivity measurement.
- **Future work:** Longitudinal tracking; linking adoption to wages/employment; firm-level adoption.

### P2. Cools & Diakopoulos (2026) — *Uses of GenAI in the Newsroom* — Journalism Practice — 300 cites
- **Objective:** Map journalists' perceptions of the perils and possibilities of GenAI tools (ChatGPT, Bard, DALL-E) in newsrooms.
- **RQ:** How do early-adopter journalists use GenAI across the news process, and what risks/opportunities do they perceive?
- **Methodology:** Qualitative study; semi-structured interviews; thematic analysis.
- **Dataset:** Interviews with journalists in the Netherlands and Denmark (self-identified early adopters).
- **Results:** **16 distinct uses** identified, concentrated in news production & distribution; use decisions driven by "journalistic intuition/gut feeling"; benefits = efficiency, data handling; perils = accuracy, credibility, algorithmic bias.
- **Limitations:** Self-selected early adopters; two Western countries; perceptions ≠ actual behavior.
- **Future work:** Journalist education/algorithmic literacy; continuous monitoring frameworks for responsible newsroom use.

### P3. Sedkaoui & Benaichouba (2026) — *GenAI as a Transformative Force for Innovation* — EJIM — 218 cites
- **Objective:** Review the literature on GenAI's innovation impact across sectors (opportunities, applications, challenges).
- **RQ:** How does GenAI drive innovation and creativity, and what challenges constrain responsible use?
- **Methodology:** Comprehensive narrative literature review.
- **Dataset:** Scientific articles published 2022–2024.
- **Results:** GenAI augments human creativity as a "collaborative partner"; transforms business models/processes with sector-varying intensity; ethical frameworks are a prerequisite.
- **Limitations:** Narrow 2022–2024 window; fast-moving field outdates findings; mostly theory-driven, few cutting-edge application studies.
- **Future work:** Continuous updating of reviews; deeper sector-specific and ethical-framework research.

### P4. Liu & Wang (2026) — *Who on Earth Is Using Generative AI?* — World Development — 163 cites
- **Objective:** First comprehensive **global** analysis of individual GenAI adoption.
- **RQ:** What are real-time global usage patterns, and which country-level factors drive uptake?
- **Methodology:** Novel data sources — website traffic analytics + Google Trends; country-level regression analysis.
- **Dataset:** Top 40 GenAI tools (~3 billion visits/month, March 2024); country covariates (income, youth share, digital infrastructure, English proficiency, human capital).
- **Results:** ChatGPT = 82.5% of traffic; users skew young/educated/male; diffusion reached almost all economies in 16 months; **middle-income economies generate >50% of traffic; low-income <1%**; uptake correlates with income, youth, infrastructure, English, human capital.
- **Limitations:** Traffic ≠ depth of use; aggregate (not individual) data; March-2024 snapshot; no productivity/outcome measures.
- **Future work:** Micro-level studies; low-income contexts; impacts on online economic activity.


### P5. Lee, Choe, Zou & Jeon (2026) — *GenAI in the Language Classroom: A Systematic Review* — Interactive Learning Environments — 158 cites
- **Objective:** Review classroom-based empirical research on GenAI for language learning.
- **RQ:** What research designs, foci, GenAI roles and challenges appear in empirical language-classroom studies?
- **Methodology:** Systematic review of 49 empirical studies (Jan 2023–Dec 2024).
- **Dataset:** 49 peer-reviewed empirical studies.
- **Results:** Higher education dominates; English is the main target language; studies rely heavily on **self-reported data**; foci = perceptions (attitude, self-efficacy, motivation) and writing; GenAI roles = feedback provider, tutor, conversation partner; challenges = content quality, overreliance, academic integrity.
- **Limitations:** 2023–24 window; primary studies' self-report bias; K-12 almost absent.
- **Future work:** K-12 contexts; longitudinal designs; **behavioral (log-based) interaction data**; customized GenAI tools.

### P6. Cheng et al. (2026) — *GenAI for Requirements Engineering: An SLR* — Software: Practice & Experience — 136 cites
- **Objective:** Systematically analyze how GenAI (LLMs) is applied to requirements engineering (RE).
- **RQ:** What are the trends, methodologies, challenges and future directions of GenAI-based RE?
- **Methodology:** SLR with systematic selection, data extraction, feature analysis.
- **Dataset:** **238 articles (2019–2025)** from major databases.
- **Results:** GPT models dominate (67.3%); RE phases unevenly covered — analysis 30.0%, elicitation 22.1%, **management only 6.8%**; core challenge triad = **reproducibility (66.8%), hallucinations (63.4%), interpretability (57.1%)**; >90% of studies early-stage; **only 1.3% production-level**; fragmented benchmarks/datasets.
- **Limitations:** Publication bias toward prototypes; rapid model evolution; evaluation-maturity gaps.
- **Future work:** Holistic (joint) mitigation of the challenge triad; public datasets/benchmarks; industrial validation.

### P7. Kim et al. (2026) — *Students–GenAI Interaction Patterns in Academic Writing* — J. Computing in Higher Education — 106 cites
- **Objective:** Identify student–AI interaction (SAI) patterns in writing tasks by **AI-literacy level**, and link patterns to writing performance.
- **RQ:** Do high- vs low-AI-literacy students interact with GenAI differently, and does it affect performance?
- **Methodology:** Mixed methods — think-aloud protocols, screen recordings, chat logs; **Epistemic Network Analysis (ENA)**; Wilcoxon tests.
- **Dataset:** 36 Chinese graduate students using a GenAI writing system.
- **Results:** High-literacy students show a **collaborative pattern** (accept suggestions, metacognitive planning); low-literacy students interact minimally and ideate alone; writing performance differs by pattern.
- **Limitations:** Small sample (n=36); graduate students only; single country/tool.
- **Future work:** Larger diverse samples; AI-literacy training interventions; other task types.

### P8. Pallant et al. (2026) — *Mastering Knowledge: GenAI & Student Learning Outcomes* — Studies in Higher Education — 105 cites
- **Objective:** Investigate how GenAI use affects student learning outcomes in higher education.
- **RQ:** Which usage approach (mastery vs. procedural) leads to higher-level learning?
- **Methodology:** Quasi-experimental design; qualitative reflections + quantitative content analysis (QCA).
- **Dataset:** 192 student reflections.
- **Results:** **Mastery approach** (construct + augment knowledge) → higher-order learning; **procedural approach** (copy-style use) → lower outcomes; curriculum and assessment should scaffold mastery goal structures.
- **Limitations:** Single course/context; self-reported reflections; short-term horizon.
- **Future work:** Assessment designs that force critical engagement; broader disciplines/institutions.


### P9. Park & Nan (2026) — *GenAI and Misinformation: A Scoping Review* — AI & Society — 70 cites
- **Objective:** Synthesize the dual role of GenAI/LLMs in misinformation generation, detection, mitigation and impact.
- **RQ:** How do LLMs generate and combat misinformation, and with what effects on users?
- **Methodology:** Scoping review.
- **Dataset:** 24 empirical studies.
- **Results:** LLMs create highly convincing misinformation exploiting cognitive biases; **the same LLMs can detect false claims and inoculate users**; mitigation = mixed results (personalized corrections work; safeguards inconsistent); exposure to AI misinformation reduces trust and alters decisions.
- **Limitations:** Few empirical studies exist; **no standardized evaluation metrics**; fast-changing safeguards.
- **Future work:** Standardized metrics; interdisciplinary collaboration; stronger regulation.

### P10. Mohammadi et al. (2026) — *Is GenAI Reshaping Academic Practices Worldwide?* — IP&M — 60 cites
- **Objective:** Map adoption, benefits and concerns of GenAI among academics globally.
- **RQ:** How do role, gender, country and discipline shape GenAI uptake in academia?
- **Methodology:** Cross-sectional international survey.
- **Dataset:** Publishing academics across **20 countries**.
- **Results:** High overall adoption; PhD students/early-career researchers adopt most; main uses = translation, proofreading, literature review (less for data analysis); top concerns = inaccuracy, plagiarism, eroded critical thinking; **females 10% less likely to be frequent users**; highest adoption in some **non-Western** nations (translation needs).
- **Limitations:** Self-reported; awareness ≠ skilled use; single time point.
- **Future work:** Track inequality effects (gender, geography); discipline-specific studies.

### P11. Daniotti, Wachs, Feng & Neffke (2026) — *Who Is Using AI to Code?* — Science — 55 cites
- **Objective:** Measure global diffusion and labor impact of GenAI coding tools.
- **RQ:** How fast and where are AI coding tools adopted, and who benefits?
- **Methodology:** Trained a **neural classifier** to detect AI-generated Python functions; diffusion + productivity estimation.
- **Dataset:** **30+ million GitHub commits by 160,097 developers**.
- **Results:** AI writes ~29% of U.S. Python functions (lead shrinking vs other countries); quarterly output +3.6%; **benefits accrue to senior developers** (productivity + domain expansion); **early-career developers show no significant benefit** → risk of widening skill gaps and reshaping career ladders.
- **Limitations:** Python/GitHub only; classifier misclassification error; commits are a proxy for productivity.
- **Future work:** Other languages/platforms; long-run career-ladder effects; entry-level job impacts.

### P12. Zhou et al. (2026) — *GenAI in Industrial Machine Vision: A Review* — J. of Intelligent Manufacturing — 52 cites
- **Objective:** Review the state of GenAI in industrial machine vision.
- **RQ:** What are recent advancements, applications and research trends?
- **Methodology:** PRISMA-guided literature review.
- **Dataset:** 1,200+ papers.
- **Results:** Primary use = **data augmentation** for classification/object detection; also super-resolution and anomaly detection for quality control; barriers = data diversity, compute requirements, lack of robust validation.
- **Limitations:** Field still early-stage; validation methods immature.
- **Future work:** Robust validation protocols; consolidated data requirements for practitioners.

### Notes on remaining corpus papers (P13–P30, used in synthesis)
- **P13 Uddin et al.** (survey): catalogs GenAI risks — deepfakes/disinformation, IP/copyright, cybersecurity, bias; covers GANs/VAEs/transformers; case studies include AI stock-prediction failure and Stable Diffusion copyright lawsuits.
- **P14 Mohamed & Aljuaid**:* proposes computing-history framing as a "trust anchor" against black-box opacity and the usability paradox.
- **P15 Heitmann et al.** (experiment): fine-tuned open-source image GenAI on marketing mindset metrics — AI visuals matched/exceeded conventional ads; notes alignment limits.
- **P16 Yu et al.** (survey, Chinese business schools): TAM-based adoption factors for students and faculty.
- **P17 Podder et al.**:* green prompt engineering — prompt design to cut GenAI's energy/carbon footprint.
- **P18 Brezovec et al.** (PRISMA SLR, 110 studies): education science frames GenAI as augmentation (71.8%); limitations: Scopus-only, English-only.
- **P19 Guo et al.**:* firm GenAI adoption → supply chain resilience (OSCM perspective).
- **P21 Singu et al.** (multi-study, tourism): framework mitigating ambiguity/anxiety toward GenAI.
- **P22 Madzík et al.** (bibliometric): LDA on 13,942 publications → 120 topics, 9 clusters, four-lane value-creation model; unresolved: ethics, security, misinformation.
- **P23 Liang et al.** (SLR, 56 studies): human–AI interaction modes (AIED-HCD framework); high human control + high automation emerging.
- **P24 Te'eni et al.** (18-month case): CORE-sandbox framework (Capabilities, Opportunities, Risks, Ecosystem) for organizational GenAI learning.
- **P25 Rahiem** (qualitative, 131 Indonesian students): AI as assistant/skill-developer/efficiency tool; fears of dependency and weakened critical thinking.
- **P26 Rismanchian et al.**:* framework of what undergraduates need to know vs. actually know about GenAI — GenAI literacy gap.
- **P28 Jia et al.** (3 studies incl. audit of 5,000 AI itineraries): 7-category socio-technical bias taxonomy for GenAI travel planners.
- **P29 Zheng et al.** (review): healthcare GenAI confined to low-risk uses; reliability, acceptance, regulation gaps.
- **P30 Montefiore et al.** (conceptual): GenAI threatens meaningfulness of creative work (deskilling, autonomy erosion) while democratizing creation.

---

## 3. Comparison Table (Top 12 papers, sorted by Scholar citations)

| # | Paper | Objective (one line) | Methodology | Dataset | Key Result | Main Limitation | Future Work |
|---|---|---|---|---|---|---|---|
| P1 | Bick et al. (Mgmt Science) | Measure speed of US GenAI adoption | National survey + historical benchmarking | RPS waves, US adults 18–64 | 39% adoption in <2 yrs; faster than PC/Internet | US-only, self-report | Longitudinal; wage/employment links |
| P2 | Cools & Diakopoulos (Journalism Practice) | Map newsroom GenAI uses & perceptions | Semi-structured interviews | Journalists, NL + DK | 16 uses; intuition-driven adoption; accuracy/bias fears | Self-selected early adopters | Algorithmic-literacy training |
| P3 | Sedkaoui & Benaichouba (EJIM) | Review GenAI innovation impact | Narrative review | 2022–24 articles | GenAI = creativity "collaborative partner" | Narrow time window | Sector-specific ethical frameworks |
| P4 | Liu & Wang (World Development) | Global map of GenAI usage | Web-traffic + Trends + regression | 40 tools, ~3B visits/mo | Diffusion in 16 months; low-income <1% of traffic | Aggregate data, 1 snapshot | Microdata; low-income studies |
| P5 | Lee et al. (ILE) | Review GenAI in language classrooms | Systematic review | 49 empirical studies | Perception-based, HE/English/writing dominate | Self-report bias; no K-12 | K-12; longitudinal; log data |
| P6 | Cheng et al. (SPE) | Review GenAI for requirements eng. | SLR | 238 articles (2019–25) | Reproducibility 67% / hallucination 63% / interpretability 57%; 1.3% production-level | Prototype publication bias | Benchmarks; industrial validation |
| P7 | Kim et al. (JCHE) | Link AI literacy to interaction patterns | Think-aloud + logs + ENA | 36 Chinese grad students | High-literacy = collaborative pattern, better writing | Small n, single context | Literacy interventions at scale |
| P8 | Pallant et al. (SHE) | GenAI's effect on learning outcomes | Quasi-experiment + QCA | 192 student reflections | Mastery use → deep learning; procedural → shallow | One course, short-term | Mastery-scaffolded assessment design |
| P9 | Park & Nan (AI & Society) | GenAI's dual role in misinformation | Scoping review | 24 empirical studies | LLMs generate AND detect misinformation; safeguards inconsistent | Few studies; no standard metrics | Standard metrics; regulation |
| P10 | Mohammadi et al. (IP&M) | Global academic GenAI adoption | Survey | Academics, 20 countries | Gender gap (−10% females); non-Western adoption high | Self-report, cross-sectional | Inequality tracking |
| P11 | Daniotti et al. (Science) | Diffusion/impact of AI coding tools | Neural classifier on commits | 30M+ commits, 160k devs | AI writes 29% of US Python; seniors gain, juniors don't | Python/GitHub only | Career-ladder effects |
| P12 | Zhou et al. (J. Intell. Manuf.) | GenAI in industrial machine vision | PRISMA review | 1,200+ papers | Data augmentation is primary use; validation weak | Immature validation methods | Validation protocols |

---

## 4. Repeated Limitations (cross-paper patterns)

| Rank | Repeated Limitation | Papers reporting it | Frequency signal |
|---|---|---|---|
| L1 | **Self-reported / perception-based data** (no behavioral logs) | P1, P2, P5, P8, P10, P16, P25 | 7+ papers — most frequent |
| L2 | **Hallucination / accuracy / reliability of outputs** | P6, P9, P10, P13, P25, P29 | 6 papers |
| L3 | **No standardized benchmarks / evaluation metrics** | P6, P9, P12, P17, P22 | 5 papers |
| L4 | **Cross-sectional snapshots; no longitudinal designs** | P1, P4, P5, P8, P10 | 5 papers |
| L5 | **Geographic / demographic bias** (Western, English, high-income, male-skewed samples or findings) | P2, P4, P5, P7, P10, P18 | 6 papers |
| L6 | **Bias, ethics, privacy, academic-integrity concerns unresolved** | P2, P3, P5, P10, P13, P22, P25, P28 | 8 papers |
| L7 | **Black-box opacity / interpretability & trust deficit** | P6, P13, P14, P21 | 4 papers |
| L8 | **Early-stage adoption — few production / real-world deployments** | P6 (1.3%), P12, P29 | 3 papers |
| L9 | **Reproducibility crisis** | P6 (66.8%), P22, P13 | 3 papers |
| L10 | **Sustainability / energy cost ignored** | P17 (only paper addressing it) | systematic silence |



## 5. Contradictions Between Papers

| # | Contradiction | Side A | Side B | Interpretation |
|---|---|---|---|---|
| C1 | **Who benefits from GenAI productivity gains?** | P11 (Science): only senior developers gain; juniors see *no* benefit → widening skill gap | P1 & P3: broad-based, fast adoption suggests democratized productivity | Gains are **skill-contingent**, not automatic — contradicts the democratization narrative |
| C2 | **Does GenAI improve or harm learning?** | P8: mastery use → higher-order learning; P7: high-AI-literacy students write better | P25 & P5: overreliance, diminished critical thinking, academic-integrity erosion | Effect depends on **usage mode and AI literacy**, which most studies don't measure |
| C3 | **Does GenAI build or erode trust?** | P14: historical framing fosters trust; P21: frameworks mitigate anxiety | P9: exposure to AI-generated misinformation *reduces* trust | Trust is malleable in both directions; no agreed calibration mechanism |
| C4 | **Is GenAI a misinformation threat or cure?** | P13: deepfakes/disinformation listed among top risks | P9: same LLMs detect false claims and inoculate users | Dual-use paradox unresolved — safeguards "inconsistently applied" (P9) |
| C5 | **Where is adoption strongest?** | P4: uptake correlates with high income, English proficiency, digital infrastructure | P10: highest academic adoption found in some **non-Western** nations | Income enables access, but **translation needs** drive intensity — a tension unexplored by both |
| C6 | **Augmentation vs. substitution of human work** | P18: education science frames 71.8% of uses as augmentation; P29: GenAI as auxiliary tool | P15: AI visuals *exceed* human-made ads; P30: deskilling, "creation → curation" shift, penalty for AI use | Discourse says augmentation; labor evidence hints at substitution |
| C7 | **Is more automation in education desirable?** | P23: high-human-control + high-AI-automation mode is an emerging positive trend | P8/P5: procedural (automation-heavy) use lowers learning outcomes | The "optimal" human–AI control balance is unsettled |

## 6. Unexplored Areas (silences across all 30 papers)

1. **K-12 and vocational education** — P5 and P18 both report higher education dominates (65.5%+); school contexts are nearly absent.
2. **Low-income / Global-South micro-level studies** — P4 shows <1% of GenAI traffic from low-income economies, yet almost no paper studies these users directly (P25 Indonesia is the lone partial exception).
3. **Longitudinal, behavioral (log-based) evidence** — nearly all human studies are one-shot self-reports (L1, L4); actual interaction logs are studied only in P7 (n=36) and P11 (code commits).
4. **Undergraduate (not graduate) AI literacy** — P7 studies grad students; P26 shows a need-vs-knowledge framework but no validated measurement instrument or intervention.
5. **Requirements-management & post-deployment phases of software engineering** — P6: only 6.8% of studies; production-level use 1.3%.
6. **Energy-aware / sustainable GenAI use** — only P17; no paper empirically measures prompt design vs. energy vs. output quality trade-offs.
7. **Standardized evaluation benchmarks** — demanded by P6, P9, P12 but created by none.
8. **Non-English GenAI performance** — P4 (English proficiency predicts uptake) and P5 (English is the dominant target language) flag it; nobody measures local-language quality.
9. **High-stakes deployment** — P29: healthcare GenAI confined to low-risk tasks; high-risk clinical use unexplored.
10. **Entry-level labor effects & interventions** — P11 identifies the junior-developer gap; no paper tests interventions to close it.

---


## 7. Research Gaps → Research Problem → RQ → Objectives → Hypothesis

### G1 — Behavioral evidence gap: how undergraduates in developing countries *actually* use GenAI
*(evidence: L1, L4, C2; unexplored areas 2, 3; papers P4, P5, P7, P25)*
- **Research Problem:** Existing studies of student–GenAI use rely on one-shot self-reports from Western/graduate samples; there is no log-verified, longitudinal evidence on how undergraduates in developing countries use GenAI for coursework, so policies against misuse are being designed on weak evidence.
- **Research Question:** How do undergraduate students in India actually use generative AI in academic work (verified by interaction logs), and which usage patterns predict better vs. poorer learning outcomes?
- **Objectives:** (1) Collect chat-log + survey data from ≥150 undergraduates over one semester; (2) classify usage patterns (mastery vs. procedural) using clustering; (3) test the association between usage pattern and grades/learning outcomes; (4) compare self-reported vs. log-verified usage.
- **Hypothesis:** H1: Mastery-oriented GenAI use is positively associated with learning outcomes, while procedural use is negatively associated. H0: GenAI usage pattern has no association with learning outcomes.

### G2 — Measurement gap: no validated GenAI-literacy instrument for undergraduates
*(evidence: C2; unexplored area 4; papers P7, P26)*
- **Research Problem:** P7 shows AI literacy changes how students benefit from GenAI, and P26 shows a gap between what undergraduates need to know and actually know — yet no validated scale exists to measure undergraduate GenAI literacy, blocking targeted interventions.
- **Research Question:** What dimensions constitute undergraduate GenAI literacy, and can a reliable, valid instrument be developed to measure it?
- **Objectives:** (1) Derive literacy dimensions from P26's framework + expert review; (2) pilot a questionnaire (n≥100); (3) establish reliability (Cronbach's α) and validity (EFA); (4) relate literacy scores to interaction quality in a writing task.
- **Hypothesis:** H1: A multi-dimensional GenAI-literacy scale (technical, ethical, evaluative, practical) will show acceptable reliability (α ≥ 0.7) and positively predict effective GenAI interaction.

### G3 — Reliability gap: no benchmark for GenAI hallucination in student coursework
*(evidence: L2, L3, L9; papers P6, P9, P13, P29)*
- **Research Problem:** Hallucination is among the most-cited GenAI risks (63.4% of RE studies, P6; top concern of academics, P10), but no public benchmark measures hallucination rates for typical undergraduate coursework tasks (assignments, code, citations), leaving students unable to judge when outputs can be trusted.
- **Research Question:** What is the hallucination/error rate of popular GenAI tools on standard undergraduate coursework tasks, and does task type or prompting strategy significantly affect it?
- **Objectives:** (1) Build a task set of ~100 coursework prompts across 4 categories (factual essays, code, references, math); (2) query 2–3 GenAI tools under 3 prompting strategies; (3) score factual accuracy via rubric + expert check; (4) compare error rates statistically.
- **Hypothesis:** H1: Hallucination rates differ significantly across task types and prompting strategies (e.g., citation-generation > code > factual prose). H0: No significant difference.

### G4 — Sustainability gap: prompt design vs. energy vs. quality trade-off is unmeasured
*(evidence: L10; paper P17)*
- **Research Problem:** P17 proposes "green prompt engineering" conceptually, but no empirical study quantifies how prompt verbosity/strategy affects token consumption (hence energy/carbon) relative to output quality, so sustainability guidance remains speculation.
- **Research Question:** How does prompt design (length, few-shot examples, chain-of-thought) affect token usage and output quality, and what is the optimal quality-per-token strategy?
- **Objectives:** (1) Design a controlled prompt experiment on a fixed task suite; (2) record input/output tokens for each strategy; (3) rate output quality blindly; (4) compute quality-per-token efficiency and recommend a "green prompt" guideline.
- **Hypothesis:** H1: Concise structured prompts achieve ≥90% of the output quality of verbose chain-of-thought prompts while consuming significantly fewer tokens.


### G5 — Literacy gap among *early-career developers*: the junior skill trap
*(evidence: C1; unexplored area 10; papers P11, P7)*
- **Research Problem:** P11 (Science) shows GenAI boosts senior developers' productivity but gives juniors no measurable benefit, threatening career ladders — yet no study tests whether structured GenAI training can convert early-career developers into beneficiaries.
- **Research Question:** Does a structured GenAI-pair-programming training module improve task performance and learning for novice programmers compared with unstructured GenAI access?
- **Objectives:** (1) Develop a short GenAI-pair-programming training module; (2) run a controlled experiment with two groups of novice programmers; (3) measure task completion time, code quality, and concept retention; (4) identify which training elements drive any gains.
- **Hypothesis:** H1: Novices receiving structured GenAI training complete programming tasks faster and with higher code quality than novices with unstructured GenAI access.

### G6 — Language gap: GenAI quality in low-resource languages for education
*(evidence: C5; unexplored area 8; papers P4, P5, P10)*
- **Research Problem:** English proficiency predicts GenAI uptake (P4) and language-education research targets English (P5), implying students working in local languages may receive lower-quality support — but no study quantifies this quality gap for low-resource languages.
- **Research Question:** How does GenAI answer quality for identical academic questions differ between English and a low-resource language (e.g., Hindi), and what error types dominate?
- **Objectives:** (1) Create a bilingual parallel question set from undergraduate syllabi; (2) collect GenAI answers in both languages; (3) evaluate accuracy/completeness with bilingual experts; (4) build an error taxonomy.
- **Hypothesis:** H1: GenAI answers in the low-resource language contain significantly more factual and completeness errors than English answers to identical questions.

### G7 — Trust-calibration gap: training users when (not) to trust GenAI
*(evidence: C3, C4; papers P9, P14, P21, P28)*
- **Research Problem:** Papers show trust in GenAI can be raised (P14, P21) or damaged (P9), but none studies *calibrated* trust — users trusting correct outputs and doubting wrong ones — leaving either over-trust (hallucination harm) or under-trust (lost productivity).
- **Research Question:** Does a brief bias/hallucination-awareness intervention improve students' trust calibration (correct acceptance/rejection of GenAI outputs) without reducing overall usage?
- **Objectives:** (1) Design a trust-calibration task with known-correct and known-wrong GenAI answers; (2) measure pre/post calibration accuracy; (3) test the effect of a short awareness module; (4) measure effects on subsequent usage intentions.
- **Hypothesis:** H1: The awareness intervention significantly improves trust-calibration accuracy without significantly reducing GenAI usage intention.

### G8 — Methods gap: GenAI-assisted systematic reviewing itself is unbenchmarked
*(evidence: L3, L9; papers P6, P18, P23, P22)*
- **Research Problem:** Reviews (P6, P18, P23) demand reproducible methods and note citation-database bias (P18 used Scopus-only, English-only), yet no work benchmarks GenAI tools themselves as SLR assistants (screening, extraction) against human reviewers.
- **Research Question:** What agreement (Cohen's κ) exists between GenAI-assisted and human title/abstract screening in an SLR, and where do the errors concentrate?
- **Objectives:** (1) Assemble a labeled screening set from a published SLR; (2) run GenAI screening under documented prompts; (3) compute agreement metrics and error classes; (4) propose a human-in-the-loop protocol.
- **Hypothesis:** H1: GenAI screening achieves substantial agreement with humans (κ ≥ 0.6) on inclusion/exclusion but errs disproportionately on interdisciplinary papers.

---


## 8. Final Recommendation — Strongest Topic for a BCA Undergraduate

### 🏆 Recommended topic (merges G1 + G2):
## **"Actual vs. Reported Use of Generative AI by Undergraduate Students in India: AI Literacy, Usage Patterns, and Learning Outcomes — A Mixed-Methods Study"**

**Why this is the strongest for a BCA student:**

| Criterion | Assessment |
|---|---|
| **Feasibility (no funding/lab)** | Survey + voluntary chat-log submission + short task — needs only Google Forms, spreadsheets, Python |
| **Skill match (BCA)** | Statistics (chi-square, t-test, correlation, Cronbach's α) + optional Python clustering — core BCA skills |
| **Access to data** | Your own college = ready sampling frame (stratified by year/section) |
| **Originality** | Directly fills L1+L4 (self-report, cross-sectional bias) and unexplored areas 2–4; only P25 (Indonesia) is comparable — **no Indian undergraduate study exists in the 2026 corpus** |
| **RM-course alignment** | Exercises the full RM pipeline: problem → RQ → objectives → hypotheses → instrument design → reliability → hypothesis testing |
| **Publishability** | Education+GenAI is the highest-cited theme in this corpus (P5, P7, P8 = 158/106/105 cites) |
| **Ethics** | Low-risk (anonymous, consented); easy institutional approval |

**Ready-to-use research design:**
- **Research Problem:** Indian higher-education institutions are framing GenAI policies without verified evidence of how undergraduates actually use GenAI or whether AI literacy moderates its learning benefits.
- **RQs:** RQ1 — What usage patterns dominate among Indian undergraduate students? RQ2 — Does GenAI literacy predict mastery-oriented (vs. procedural) use? RQ3 — Which pattern is associated with better academic performance?
- **Objectives:** (1) Adapt/validate a GenAI-literacy scale for undergraduates; (2) profile usage patterns via survey + chat logs; (3) test literacy → pattern → outcome relationships.
- **Hypotheses:** H1: Higher GenAI literacy predicts mastery-oriented use. H2: Mastery-oriented users show higher academic performance than procedural users. H3: Self-reported usage diverges significantly from log-verified usage.
- **Methodology:** Mixed methods; stratified random sample n≥150; instruments = literacy scale (validate: α, EFA) + usage questionnaire + optional chat-log diaries over 4 weeks + GPA; analysis = descriptive statistics, χ², t-tests, correlation/regression; optional k-means clustering of usage patterns.
- **Expected contribution:** First Indian undergraduate GenAI-literacy + behavior dataset; evidence-based policy recommendations for colleges; a validated short literacy scale others can reuse.

**Runner-up (if you prefer a pure-experiment, zero-human-subjects project):** G4 — *Green Prompt Engineering: an empirical quality-per-token study* (needs only free GenAI APIs + Python; directly extends P17, a timely but barely-explored direction).

---


## 9. References (top-12 analyzed papers + key corpus papers)

1. Bick, A., Blandin, A., & Deming, D. J. (2026). The rapid adoption of generative AI. *Management Science* (NBER WP 33255/32966). https://pubsonline.informs.org/doi/abs/10.1287/mnsc.2025.02523
2. Cools, H., & Diakopoulos, N. (2026). Uses of generative AI in the newsroom: Mapping journalists' perceptions of perils and possibilities. *Journalism Practice, 20*(3), 878–896. https://doi.org/10.1080/17512786.2024.2394558
3. Sedkaoui, S., & Benaichouba, R. (2026). Generative AI as a transformative force for innovation: a review of opportunities, applications and challenges. *European Journal of Innovation Management, 29*(3). https://doi.org/10.1108/EJIM-02-2024-0129
4. Liu, Y., & Wang, H. (2026). Who on Earth is using generative AI? *World Development* (World Bank Policy Research WP 10870). https://doi.org/10.1596/1813-9450-10870
5. Lee, S., Choe, H., Zou, D., & Jeon, J. (2026). Generative AI (GenAI) in the language classroom: A systematic review. *Interactive Learning Environments*. https://doi.org/10.1080/10494820.2025.2498537
6. Cheng, H., Husen, J. H., Lu, Y., Racharak, T., et al. (2026). Generative AI for requirements engineering: A systematic literature review. *Software: Practice and Experience*. https://doi.org/10.1002/spe.70029
7. Kim, J., Lee, S. S., Detrick, R., Wang, J., & Li, N. (2026). Students–generative AI interaction patterns and its impact on academic writing. *Journal of Computing in Higher Education*. https://doi.org/10.1007/s12528-025-09444-6
8. Pallant, J. L., Blijlevens, J., Campbell, A., et al. (2026). Mastering knowledge: The impact of generative AI on student learning outcomes. *Studies in Higher Education*. https://doi.org/10.1080/03075079.2025.2487570
9. Park, S., & Nan, X. (2026). Generative AI and misinformation: a scoping review. *AI & Society*. https://doi.org/10.1007/s00146-025-02620-3
10. Mohammadi, E., Thelwall, M., Cai, Y., Collier, T., et al. (2026). Is generative AI reshaping academic practices worldwide? *Information Processing & Management*. https://doi.org/10.1016/j.ipm.2025.104350
11. Daniotti, S., Wachs, J., Feng, X., & Neffke, F. (2026). Who is using AI to code? Global diffusion and impact of generative AI. *Science, 391*(6787), 831–835. https://doi.org/10.1126/science.adz9311
12. Zhou, H. A., Wolfschläger, D., Florides, C., et al. (2026). Generative AI in industrial machine vision: a review. *Journal of Intelligent Manufacturing, 37*, 1447–1470. https://doi.org/10.1007/s10845-025-02604-6
13. Uddin, M., Arfeen, S. U., Alanazi, F., Hussain, S., Mazhar, T., & Rahman, M. A. (2026). A critical analysis of generative AI. *Archives of Computational Methods in Engineering, 33*, 1763–1793. https://doi.org/10.1007/s11831-025-10355-z
14. Mohamed, M., & Aljuaid, F. (2026). Historical context as a trust anchor. *Information and Software Technology*. https://doi.org/10.1016/j.infsof.2026.108274
15. Heitmann, M., Jansen, T. P. J., Reisenbichler, M., et al. (2026). Picture perfect: Engaging customers with visual generative AI. *Journal of Marketing*. https://doi.org/10.1177/00222429251356993
16. Yu, T., Dai, J., Chen, X., & Wang, C. (2026). To use or not to use? Generative AI adoption in Chinese business schools. *The International Journal of Management Education*. https://doi.org/10.1016/j.ijme.2025.101323
17. Podder, S., Date, H., & Murthy, S. (2026). Green prompt engineering for sustainable generative AI. *Environmental Science and Ecotechnology*. https://doi.org/10.1016/j.ese.2026.100684
18. Brezovec, E., Zelić, M., & Zagode, A. M. (2026). Stabilizing truth in educational sciences. *Kybernetes, 55*(13). https://doi.org/10.1108/K-09-2025-2339
19. Liang, Z., Yang, K., Sha, L., Gašević, D., et al. (2026). A systematic review of generative AI in education. *British Journal of Educational Technology*. https://doi.org/10.1111/bjet.70055
20. Te'eni, D., Raymond, M., Rowe, F., Thénoz, E., et al. (2026). Organizational learning for exploring Generative AI: CORE-sandbox experiments. *International Journal of Information Management*. https://doi.org/10.1016/j.ijinfomgt.2026.103029
21. Rahiem, M. D. H. (2026). Generative AI in higher education in Indonesia. *Social Sciences & Humanities Open*. https://doi.org/10.1016/j.ssaho.2026.102672
22. Rismanchian, S., Babar, E. T. R., & Doroudi, S. (2026). What undergraduate students need to know and actually know about generative AI. *Computers and Education: Artificial Intelligence*. https://doi.org/10.1016/j.caeai.2026.100554
23. Jia, S., Ma, C., Chi, O. H., & Fan, A. (2026). A socio-technical exploration of bias in generative AI travel planners. *Tourism Management*. https://doi.org/10.1016/j.tourman.2026.105442
24. Zheng, J., Li, B., Li, H., & Lu, Y. (2026). Generative AI in healthcare. *Journal of Management Analytics*. https://doi.org/10.1080/23270012.2026.2647940
25. Montefiore, T., Formosa, P., Bankins, S., et al. (2026). The impacts of generative AI on the meaningfulness of creative work. *Journal of Business Ethics*. https://doi.org/10.1007/s10551-026-06342-4

## 10. Appendix — Data Collection Notes

- **Playwright scraper** (headless Chromium): `scrape.js` → `slr_results.json` (30 Scholar records: title, authors, venue, snippet, citation count).
- **Abstract harvester**: `fetch_abstracts.js` → `abstracts.json` (publisher meta-tags; ScienceDirect/Emerald/Wiley/Sage blocked by bot-walls — noted honestly).
- **API resolvers**: `fetch_oa.js` / `fix_oa.js` / `fix_crossref.js` → `oa_papers.json` + `digest.json` (verified abstracts via OpenAlex & Crossref; Semantic Scholar attempted but rate-limited).
- **Database access issues:** ACM Digital Library returned HTTP 403 (bot detection); IEEE Xplore returned an obfuscated anti-bot page. Springer and Google Scholar were accessible. This limitation is documented per SLR reporting standards (PRISMA flow transparency).
- All raw data retained in `.slr/` for reproducibility and audit.
