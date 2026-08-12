# ML Pipeline Results

Cleaned samples: 481, features: 46

**H0 (usage hours vs distress): r=0.330, p=0.0000**

## Regression (5-fold CV)
| Model                      |    R2 |   MAE |   RMSE |
|:---------------------------|------:|------:|-------:|
| Multiple Linear Regression | 0.388 | 0.808 |  1.018 |
| Decision Tree Regressor    | 0.337 | 0.845 |  1.06  |
| Random Forest Regressor    | 0.445 | 0.791 |  0.971 |
| KNN Regressor              | 0.334 | 0.891 |  1.066 |

## Classification (5-fold CV)
| Model               | BestParams                                                                          |   Accuracy |   Precision |   Recall |    F1 |
|:--------------------|:------------------------------------------------------------------------------------|-----------:|------------:|---------:|------:|
| Logistic Regression | {'model__C': 0.01}                                                                  |      0.624 |       0.568 |    0.546 | 0.521 |
| Decision Tree       | {'model__max_depth': None, 'model__min_samples_split': 2}                           |      0.547 |       0.514 |    0.512 | 0.511 |
| Random Forest       | {'model__max_depth': 10, 'model__min_samples_split': 2, 'model__n_estimators': 100} |      0.626 |       0.541 |    0.552 | 0.523 |
| KNN                 | {'model__n_neighbors': 11, 'model__weights': 'distance'}                            |      0.601 |       0.571 |    0.549 | 0.55  |

Best K-Means k=2

## Top 10 Features
|                                                                 |   importance |
|:----------------------------------------------------------------|-------------:|
| How_much_are_you_bothered_by_worries                            |    0.100066  |
| What_is_your_age                                                |    0.0748845 |
| How_frequently_does_your_interest_in_daily_activities_fluctuate |    0.0669499 |
| Do_you_find_it_difficult_to_concentrate_on_things               |    0.0622014 |
| How_often_do_you_compare_yourself_to_other_successful_people    |    0.0566109 |
| NumPlatforms                                                    |    0.0522921 |
| UsageHoursPerDay                                                |    0.0520318 |
| How_often_do_you_face_issues_regarding_sleep                    |    0.0487739 |
| Do_you_look_to_seek_validation_from_features_of_social_media    |    0.044257  |
| Do_you_feel_restless_if_you_havent_used_Social_media            |    0.0430876 |
