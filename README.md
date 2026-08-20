# UberEats ML Capstone

## End-to-End Machine Learning, NLP, Segmentation, Regression & Demand Forecasting

An end-to-end machine learning capstone project built around a synthetic
Uber Eats--style dataset. The project progresses from data generation
and validation through customer/restaurant segmentation,
customer-feedback sentiment analysis, delivery-time regression, hourly
demand forecasting, business insight generation, and final
Git/presentation preparation.

------------------------------------------------------------------------

## 1. Project Overview

### Business Problem

An Uber Eats--style food delivery platform needs to understand its
customers, restaurants, delivery operations, customer feedback, and
demand patterns in order to improve:

-   Customer retention and value
-   Restaurant performance
-   Delivery reliability
-   Customer experience
-   Operational capacity planning
-   Demand forecasting
-   Data-driven decision making

The capstone combines multiple machine-learning approaches to answer
these questions:

1.  **Who are the most valuable customer segments?**
2.  **Which restaurant groups need attention or intervention?**
3.  **What are the major causes of negative customer experiences?**
4.  **Which factors are associated with delivery time?**
5.  **When is demand highest, and when should additional delivery
    capacity be planned?**

------------------------------------------------------------------------

## 2. Project Learning Journey

``` text
Day 1
Data Generation + Data Validation + Git
        |
        v
Day 2
Customer & Restaurant Segmentation
K-Means + DBSCAN + PCA
        |
        v
Day 3
NLP Customer Feedback Analysis
Cleaning + TF-IDF + Naive Bayes + VADER
        |
        v
Day 4
Delivery Time Prediction
Linear Regression + Ridge + Lasso + Random Forest
        |
        v
Day 5
Hourly Demand Forecasting
Decomposition + ADF + ARIMA + Prophet
        |
        v
Day 6
End-to-End ML Pipeline + Business Insights
        |
        v
Day 7
Finalization + Git Workflow + Presentation
```

------------------------------------------------------------------------

# 3. Dataset

The project uses synthetic Uber Eats--style data generated for the
capstone.

## Core Order Dataset

The main order dataset contains **10,000 orders**.

Important fields include:

  Column              Description
  ------------------- --------------------------------------
  `order_id`          Unique order identifier
  `customer_id`       Customer identifier
  `restaurant_id`     Restaurant identifier
  `order_timestamp`   Date and time of the order
  `order_amount`      Order value
  `number_of_items`   Number of items in the order
  `order_status`      Delivered, Cancelled, or In Progress

The order data spans approximately:

**2026-01-01 → 2026-03-30**

Observed order status counts:

-   Delivered: **8,481**
-   Cancelled: **1,030**
-   In Progress: **489**

The delivered orders are used for delivery-specific analysis because
they have completed delivery records.

------------------------------------------------------------------------

# 4. Project Structure

The repository is organized into data, models, notebooks, outputs, and
documentation.

``` text
UberEats/
│
├── data/
│   ├── raw/
│   │   └── synthetic source datasets
│   │
│   └── processed/
│       ├── cleaned_reviews.csv
│       ├── tfidf_reviews.csv
│       ├── delivery_prediction_features.csv
│       ├── hourly_demand.csv
│       └── hourly_demand_features.csv
│
├── models/
│   ├── sentiment_naive_bayes.pkl
│   ├── tfidf_vectorizer.pkl
│   ├── arima_demand_model.pkl
│   └── prophet_demand_model.pkl
│
├── notebooks/
│   ├── 01_*.ipynb
│   ├── 02_*.ipynb
│   ├── 03_customer_feedback_nlp.ipynb
│   ├── 04_*.ipynb
│   ├── 05_*.ipynb
│   └── 06_*.ipynb
│
├── outputs/
│   ├── day2/
│   ├── day3/
│   ├── day4/
│   ├── day5/
│   └── day6/
│
├── README.md
└── .gitignore
```

> Exact notebook filenames may vary depending on the final repository
> state. The important convention is to keep each day's analysis,
> models, and outputs clearly separated.

------------------------------------------------------------------------

# 5. Day 1 -- Data Generation, Validation & Project Setup

## Objective

Establish the project foundation and create a reliable synthetic
dataset.

## Main Activities

-   Project/repository initialization
-   Synthetic data generation
-   Data validation
-   Schema checks
-   Missing-value checks
-   Data consistency checks
-   Initial EDA
-   Git setup

## Data Quality Validation

Important checks included:

-   Dataset shape
-   Column names
-   Missing values
-   Duplicate records
-   Valid timestamps
-   Valid order status values
-   Relationship between orders and delivery records
-   Delivered-order consistency

A key validation result was:

``` text
Orders:              10,000
Delivered orders:     8,481
Delivery records:     8,481
```

This confirms that every delivered order in the validated dataset has a
corresponding delivery record.

------------------------------------------------------------------------

# 6. Day 2 -- Customer & Restaurant Segmentation

## Objective

Use unsupervised learning to identify meaningful groups of customers and
restaurants.

## Techniques

### K-Means

K-Means was used to group observations based on behavioral/performance
features.

### DBSCAN

DBSCAN was used as an alternative clustering approach capable of
identifying dense groups and potential outliers.

### PCA

Principal Component Analysis was used for dimensionality reduction and
visualization.

## Customer Segmentation Features

The customer segmentation work included variables such as:

-   `total_orders`
-   `avg_order_value`
-   `total_spending`
-   `active_months`
-   `ordering_frequency`
-   `weekend_orders`
-   `late_night_orders`
-   `avg_rating_given`

The customer segmentation dataset contained **1,000 customers** with
engineered behavioral features.

## Restaurant Segmentation

Restaurant-level analysis considered performance indicators including:

-   Total orders
-   Revenue
-   Average rating
-   Average preparation time
-   Average delivery time
-   Cancellation rate
-   Restaurant count

An observed restaurant cluster summary included:

  ---------------------------------------------------------------------------------------
    Cluster    Total     Revenue      Avg Avg Prep        Avg   Cancellation   Restaurant
              Orders               Rating     Time   Delivery           Rate        Count
                                                         Time                
  --------- -------- ----------- -------- -------- ---------- -------------- ------------
          0    43.83   46,387.86     3.85    25.56      84.49           0.11           46

          1    51.49   54,809.98     3.72    28.56      89.87           0.13           37

          2    57.29   62,510.49     3.90    26.41      85.43           0.10           56

          3    47.07   50,476.82     3.96    27.97      88.24           0.08           61
  ---------------------------------------------------------------------------------------

### Business Interpretation

Cluster interpretation should be based on relative behavior rather than
treating cluster numbers as inherently meaningful.

For example:

-   A high-revenue/high-order cluster can represent valuable restaurant
    groups.
-   A cluster with high cancellation and delivery/preparation times can
    indicate operational intervention opportunities.
-   A cluster with strong ratings and lower cancellation can represent
    operationally healthier restaurants.

------------------------------------------------------------------------

# 7. Day 3 -- NLP Customer Feedback Analysis

## Objective

Convert unstructured customer reviews into measurable sentiment and
complaint insights.

## NLP Pipeline

``` text
Raw Review
    |
    v
Text Cleaning
    |
    v
Cleaned Review
    |
    v
TF-IDF Vectorization
    |
    +------------------+
    |                  |
    v                  v
Naive Bayes         VADER
Classification      Sentiment
    |
    v
Evaluation + Complaint Themes
```

## Review Dataset

The validated review set contained:

**8,481 reviews**

The project also used a small set of unique/template review texts to
construct and validate the sentiment workflow.

Examples included:

-   "Food quality was disappointing."
-   "Food was amazing and arrived hot."
-   "Delivery was very late."
-   "Nothing special but it was fine."
-   "Great experience, will order again."

## Text Preprocessing

The preprocessing stage removed unnecessary textual noise and produced
cleaned review text.

Examples:

  Original                              Cleaned
  ------------------------------------- ------------------------------
  Food quality was disappointing.       `food quality disappointing`
  Food was amazing and arrived hot.     `food amazing arrived hot`
  Delivery was very late.               `delivery late`
  Great experience, will order again.   `great experience order`

Validation showed:

``` text
Original reviews:          8,481
Missing cleaned reviews:       0
Empty cleaned reviews:         0
```

## TF-IDF

TF-IDF was used to convert cleaned reviews into numerical features.

The validated training/testing template split produced:

``` text
Training TF-IDF shape: (11, 47)
Testing TF-IDF shape:  (6, 47)

Vocabulary size: 47
```

## Sentiment Classification

A Naive Bayes sentiment model was implemented and saved as:

``` text
models/sentiment_naive_bayes.pkl
```

The TF-IDF vectorizer was saved as:

``` text
models/tfidf_vectorizer.pkl
```

### Important Model Evaluation

The template-based supervised evaluation produced relatively weak
generalization:

``` text
Accuracy : 0.1667
Precision: 0.0833
Recall   : 0.1667
F1-score : 0.1111
```

This result is important and should not be hidden in the final
presentation. The small template dataset and limited vocabulary make the
supervised model evaluation much less reliable than evaluation on a
large, independently labeled dataset.

## VADER

VADER was also evaluated on the broader review set.

Observed results:

``` text
Accuracy : 0.8361
Precision: 0.8324
Recall   : 0.8361
F1-score : 0.8194
```

Class-level performance showed particularly strong positive-sentiment
detection, while negative and neutral classes were more difficult to
separate.

## Complaint Theme Analysis

The major complaint themes were:

  Complaint Theme             Review Count   Percentage
  ------------------------- -------------- ------------
  Delivery Delays                      371       33.39%
  Food Quality/Freshness               366       32.94%
  Food Arrived Cold                    192       17.28%
  Poor Overall Experience              182       16.38%

### Key Business Insight

**Delivery delays and food quality/freshness are the two largest
complaint categories**, each representing roughly one-third of the
classified complaint themes.

This provides a direct connection between the NLP analysis and the
delivery-time prediction/forecasting work.

------------------------------------------------------------------------

# 8. Day 4 -- Delivery Time Prediction

## Objective

Predict `delivery_time_minutes` using supervised regression.

## Target

``` text
delivery_time_minutes
```

The delivery dataset contained **8,481 delivered orders**.

Target distribution:

``` text
Count:  8,481
Mean:      86.88 minutes
Std:       21.83 minutes
Min:       21 minutes
Median:    87 minutes
75%:      103 minutes
Max:      156 minutes
```

There were:

``` text
Missing delivery times: 0
```

## Features

The regression workflow included features such as:

-   Delivery distance
-   Preparation time
-   Order amount
-   Number of items
-   Restaurant rating
-   Traffic condition
-   Weather
-   Order hour
-   Day of week
-   Restaurant category

Categorical variables were encoded through preprocessing.

## Models

At least four regression approaches were evaluated:

1.  Linear Regression
2.  Ridge Regression
3.  Lasso Regression
4.  Random Forest Regression

## Test Results

  Model                    MAE     RMSE       R²
  ------------------- -------- -------- --------
  Ridge Regression      4.0250   5.0255   0.9452
  Linear Regression     4.0252   5.0256   0.9452
  Lasso Regression      4.0358   5.0418   0.9448
  Random Forest         4.4706   5.5748   0.9325

## Cross-Validation

Cross-validation RMSE results:

  Model                 Mean CV RMSE   CV Std
  ------------------- -------------- --------
  Ridge Regression            5.0430   0.0672
  Linear Regression           5.0430   0.0672
  Lasso Regression            5.0730   0.0706
  Random Forest               5.7642   0.1145

### Best Model

**Ridge Regression** was selected as the preferred model because it
achieved the best overall combination of test performance and
cross-validation performance.

Its performance was extremely close to ordinary Linear Regression, while
regularization provides additional protection against unstable
coefficients in the presence of correlated features.

## Feature Importance

The Random Forest feature analysis identified the following major
contributors:

  Feature               Importance
  ------------------- ------------
  Delivery distance         0.5766
  Preparation time          0.2229
  Traffic -- Low            0.0501
  Traffic -- High           0.0451
  Weather -- Stormy         0.0226
  Traffic -- Medium         0.0138
  Weather -- Clear          0.0129
  Weather -- Rainy          0.0121

### Business Interpretation

Delivery distance and preparation time dominate the model's
feature-importance analysis.

This suggests that operational improvements should focus heavily on:

-   Better restaurant preparation-time management
-   Smarter restaurant/rider matching
-   Delivery-zone planning
-   Route and dispatch optimization

Traffic and weather are also relevant, but their contribution is
substantially smaller than distance and preparation time in this
dataset.

------------------------------------------------------------------------

# 9. Day 5 -- Hourly Demand Forecasting

## Objective

Forecast future order demand using time-series methods.

## Target

``` text
Hourly order volume
```

The order dataset was aggregated into hourly demand.

The resulting hourly dataset contained:

**2,136 hourly observations**

The observed period was approximately:

``` text
2026-01-01 00:00
→
2026-03-30 23:00
```

## Dataset Preparation

Hourly aggregation converted individual orders into:

``` text
timestamp → order_count
```

Example:

``` text
2026-01-01 00:00 → 3
2026-01-01 01:00 → 4
2026-01-01 02:00 → 6
```

## Exploratory Analysis

The analysis examined:

-   Hour-of-day patterns
-   Weekday/weekend behavior
-   Day-of-week demand
-   Peak hours
-   Trend
-   Seasonality

Observed average hourly demand was relatively stable, with differences
between hours rather than a dramatic single peak.

## Weekend vs Weekday

Observed average demand:

  Day Type     Mean Hourly Demand
  ---------- --------------------
  Weekday                  3.9921
  Weekend                  3.9183

The difference is small, suggesting that this synthetic dataset does not
show a strong weekend uplift.

## Day-of-Week Profile

  Day           Mean Hourly Demand
  ----------- --------------------
  Monday                    3.9391
  Tuesday                   3.9132
  Wednesday                 3.8750
  Thursday                  4.1250
  Friday                    4.0929
  Saturday                  3.7628
  Sunday                    4.0737

Thursday had the highest observed average hourly demand among the
weekdays in this analysis.

## Peak Hours

The highest observed hourly average profiles included:

     Hour   Mean Demand
  ------- -------------
    09:00        4.3371
    17:00        4.3034
    06:00        4.2809
    15:00        4.2247
    10:00        4.2022

These should be interpreted as dataset-specific demand patterns rather
than universal Uber Eats behavior.

------------------------------------------------------------------------

# 10. Time-Series Decomposition

The hourly demand series was decomposed into:

``` text
Observed
Trend
Seasonal
Residual
```

A seasonal period of **24 hours** was used to examine daily hourly
seasonality.

The project includes:

``` text
outputs/day5/time_series_decomposition.png
```

and related decomposition output.

------------------------------------------------------------------------

# 11. Stationarity & ADF Test

The Augmented Dickey-Fuller test was used to assess stationarity.

Observed result:

``` text
ADF Statistic: -31.8614
p-value:       0.0
```

The extremely small p-value indicates rejection of the null hypothesis
of a unit root for the original hourly series.

A differencing check was also performed:

``` text
Differenced ADF Statistic: -15.9206
Differenced p-value: 7.93e-29
```

This provided the statistical basis for the ARIMA workflow.

------------------------------------------------------------------------

# 12. ARIMA Forecasting

## Chronological Split

The time series was split chronologically rather than randomly.

``` text
Train:
2026-01-01 00:00
→
2026-03-13 03:00

Test:
2026-03-13 04:00
→
2026-03-30 23:00
```

The test period contained:

**428 observations**

## Model

An ARIMA(1,1,1) model was implemented.

Key model diagnostics included:

``` text
AR(1) coefficient ≈ -0.0483
MA(1) coefficient ≈ -0.9970
```

The model was saved as:

``` text
models/arima_demand_model.pkl
```

## ARIMA Evaluation

``` text
MAE  : 1.6103
RMSE : 2.0260
MAPE : 49.8045%
```

------------------------------------------------------------------------

# 13. Prophet Forecasting

Prophet was used as a second forecasting approach, with hourly/daily and
weekly seasonality considered in the forecasting workflow.

The model was saved as:

``` text
models/prophet_demand_model.pkl
```

## Prophet Evaluation

``` text
MAE  : 1.5861
RMSE : 2.0174
MAPE : 48.1545%
```

## ARIMA vs Prophet

  Model          MAE     RMSE       MAPE
  --------- -------- -------- ----------
  ARIMA       1.6103   2.0260   49.8045%
  Prophet     1.5861   2.0174   48.1545%

### Best Forecasting Model

**Prophet** performed slightly better than ARIMA across MAE, RMSE, and
MAPE on the chronological test period.

The difference is small, so the result should be interpreted as a
dataset-specific performance comparison rather than proof that Prophet
is universally superior.

------------------------------------------------------------------------

# 14. Day 6 -- End-to-End ML Pipeline & Business Insights

## Objective

Integrate the outputs from the individual ML components and translate
them into actionable business decisions.

The conceptual pipeline is:

``` text
Raw Data
   |
   v
Data Cleaning
   |
   v
Feature Engineering
   |
   +-------------------+
   |                   |
   v                   v
Segmentation          NLP
   |                   |
   v                   v
Customer/Restaurant   Sentiment &
Clusters              Complaint Themes
   |                   |
   +---------+---------+
             |
             v
       Delivery Prediction
             |
             v
       Demand Forecasting
             |
             v
       Business Insights
             |
             v
       Recommendations
```

------------------------------------------------------------------------

# 15. Integrated Business Insights

## 15.1 Customer Value

Customer segmentation provides a framework for identifying groups with
different ordering behavior and spending patterns.

The most valuable segments should be identified by comparing:

-   Total orders
-   Total spending
-   Average order value
-   Ordering frequency
-   Active months

### Business Action

High-value/high-frequency customers can be prioritized for:

-   Retention campaigns
-   Personalized offers
-   Loyalty programs
-   Early access to promotions

------------------------------------------------------------------------

## 15.2 Restaurant Intervention

Restaurant segmentation combines:

-   Revenue
-   Order volume
-   Rating
-   Preparation time
-   Delivery time
-   Cancellation rate

A restaurant cluster with high demand but poor operational indicators
can be prioritized for intervention.

### Business Action

Potential interventions include:

-   Restaurant preparation-time improvement
-   Operational coaching
-   Menu/process optimization
-   Delivery-zone adjustments
-   Monitoring of cancellation rates

------------------------------------------------------------------------

## 15.3 Customer Experience

The NLP complaint analysis identified:

1.  Delivery Delays -- **33.39%**
2.  Food Quality/Freshness -- **32.94%**
3.  Food Arrived Cold -- **17.28%**
4.  Poor Overall Experience -- **16.38%**

### Business Action

The first priority should be reducing delivery delays and improving food
freshness/quality because together they account for roughly two-thirds
of the classified complaint themes.

------------------------------------------------------------------------

## 15.4 Delivery Time Drivers

Random Forest feature analysis showed:

``` text
Delivery distance        57.66%
Preparation time          22.29%
Traffic variables          ~10.90% combined
Weather variables          ~5.0% combined
Other variables            remaining contribution
```

### Business Action

Operational teams should focus on distance and preparation time first.

Possible actions:

-   Improve dispatch/routing
-   Optimize delivery zones
-   Reduce restaurant preparation variability
-   Monitor restaurants with consistently long preparation times
-   Increase operational support during difficult traffic/weather
    conditions

------------------------------------------------------------------------

## 15.5 Demand Capacity Planning

The forecasting workflow provides a mechanism for estimating future
hourly order volume.

The observed dataset showed:

-   Similar weekday and weekend average hourly demand
-   Higher average demand around selected hours
-   Thursday/Friday/Sunday among stronger days in the observed profile
-   Peak hourly profiles around 09:00, 17:00, 06:00, 15:00 and 10:00

### Business Action

Capacity planning can use forecasted demand to:

-   Increase rider availability during predicted high-demand periods
-   Pre-position drivers in high-demand areas
-   Monitor restaurant preparation capacity
-   Prepare customer-service capacity
-   Reduce expected delivery delays during demand peaks

------------------------------------------------------------------------

# 16. Model Comparison Summary

## NLP

  -----------------------------------------------------------------------
  Approach                            Result
  ----------------------------------- -----------------------------------
  Naive Bayes                         Useful supervised baseline, but
                                      weak template-based evaluation

  VADER                               Stronger performance on the broader
                                      review set

  Complaint themes                    Directly useful for business
                                      prioritization
  -----------------------------------------------------------------------

## Delivery Regression

  Model                MAE     RMSE       R²
  --------------- -------- -------- --------
  Ridge             4.0250   5.0255   0.9452
  Linear            4.0252   5.0256   0.9452
  Lasso             4.0358   5.0418   0.9448
  Random Forest     4.4706   5.5748   0.9325

**Preferred:** Ridge Regression.

## Demand Forecasting

  Model          MAE     RMSE       MAPE
  --------- -------- -------- ----------
  ARIMA       1.6103   2.0260   49.8045%
  Prophet     1.5861   2.0174   48.1545%

**Preferred:** Prophet, based on the observed chronological test
metrics.

------------------------------------------------------------------------

# 17. Model Limitations

The project is a capstone based on synthetic data, so the results should
be interpreted as a demonstration of the ML workflow rather than
production Uber Eats performance.

## Data Limitations

-   Synthetic data may not reproduce real-world behavior.
-   The dataset covers approximately three months.
-   Demand history is relatively short for robust long-term seasonality
    analysis.
-   Geographic and operational effects may be simplified.
-   External events and holidays are not comprehensively modeled.

## NLP Limitations

-   The supervised sentiment template dataset is very small.
-   The template-based Naive Bayes evaluation produced low performance.
-   VADER is lexicon/rule based and can struggle with domain-specific
    language, sarcasm, and nuanced reviews.
-   Complaint themes are based on predefined categories rather than a
    fully learned topic model.

## Regression Limitations

-   Delivery time depends on factors that may not exist in the synthetic
    dataset.
-   Feature importance does not establish causality.
-   Random Forest underperformed the linear/regularized models in this
    experiment.
-   Model performance may change substantially on real-world data.

## Forecasting Limitations

-   Only a relatively short historical period is available.
-   MAPE is sensitive to small/zero demand values.
-   Hourly demand is low-count data, making percentage errors appear
    large.
-   Forecast performance is specific to the synthetic demand-generating
    process.
-   No large-scale external holiday/event dataset was incorporated.

------------------------------------------------------------------------

# 18. Future Improvements

## Data

-   Use real historical order data.
-   Add latitude/longitude or delivery zones.
-   Add driver availability.
-   Add restaurant operating hours.
-   Add weather APIs.
-   Add traffic APIs.
-   Add holidays and major events.
-   Extend the historical period.

## Segmentation

-   Tune K-Means using multiple cluster-quality metrics.
-   Compare additional clustering algorithms.
-   Build segment-specific retention models.
-   Track segment migration over time.

## NLP

-   Build a larger manually labeled sentiment dataset.
-   Use transformer-based sentiment models.
-   Apply topic modeling to discover complaint themes automatically.
-   Add aspect-based sentiment analysis.
-   Detect emerging complaint categories.

## Delivery Prediction

-   Add driver-level features.
-   Add route distance/travel time.
-   Add restaurant workload.
-   Add real-time traffic.
-   Tune hyperparameters using cross-validation.
-   Compare additional algorithms such as Gradient Boosting/XGBoost
    where appropriate.

## Forecasting

-   Extend the time history.
-   Test multiple seasonal periods.
-   Add external regressors.
-   Evaluate SARIMA/SARIMAX and other forecasting approaches.
-   Consider hierarchical forecasts by city, zone, restaurant category,
    or hour.
-   Use rolling-origin backtesting rather than a single holdout period.

## Productionization

-   Convert notebooks into reusable Python modules.
-   Add automated data validation.
-   Add unit/integration tests.
-   Add experiment tracking.
-   Add model versioning.
-   Add scheduled retraining.
-   Add monitoring for data drift and model drift.
-   Build a dashboard for business users.

------------------------------------------------------------------------

# 19. Reproducibility

The project is organized so that the analysis can be reproduced from the
repository.

Important reproducibility practices include:

-   Fixed project structure
-   Explicit processed datasets
-   Saved ML models
-   Saved vectorizers
-   Saved forecast outputs
-   Saved evaluation tables
-   Saved visualizations
-   Notebook-based analysis
-   Git version control

Important saved models include:

``` text
models/sentiment_naive_bayes.pkl
models/tfidf_vectorizer.pkl
models/arima_demand_model.pkl
models/prophet_demand_model.pkl
```

------------------------------------------------------------------------

# 20. Key Output Files

## Day 3

``` text
outputs/day3/
├── complaint_themes.csv
├── confusion_matrix.png
├── vader_confusion_matrix.png
├── sentiment_model_evaluation.csv
├── top_negative_terms.csv
└── top_positive_terms.csv
```

## Day 4

Typical outputs include:

``` text
outputs/day4/
├── model comparison results
├── feature importance
├── actual vs predicted visualization
├── regression evaluation
└── prediction/error analysis
```

## Day 5

The forecasting workflow produced:

``` text
outputs/day5/
├── adf_test_results.csv
├── arima_forecast.csv
├── forecast_comparison.png
├── forecast_summary.csv
├── model_comparison.csv
├── prophet_forecast.csv
├── prophet_forecast.png
└── time_series_decomposition.png
```

Processed demand datasets:

``` text
data/processed/
├── hourly_demand.csv
└── hourly_demand_features.csv
```

------------------------------------------------------------------------

# 21. Suggested Environment

The project was developed in a Python virtual environment.

Typical dependencies include:

``` text
Python 3.12
pandas
numpy
matplotlib
seaborn
scikit-learn
statsmodels
Prophet
nltk
joblib
jupyter
```

Install dependencies from the project's dependency file if one is
present:

``` bash
pip install -r requirements.txt
```

If a requirements file is not present, install the libraries used by the
notebooks in the active virtual environment.

------------------------------------------------------------------------

# 22. Running the Project

Activate the virtual environment:

``` bash
source .venv/bin/activate
```

Start Jupyter:

``` bash
jupyter notebook
```

Run the notebooks in chronological order:

``` text
Day 1
  ↓
Day 2
  ↓
Day 3
  ↓
Day 4
  ↓
Day 5
  ↓
Day 6
```

This order is recommended because later analyses use processed data and
outputs created by earlier stages.

------------------------------------------------------------------------

# 23. Git Workflow

The project uses a feature branch:

``` text
feature/uber-eats-pipeline
```

Typical workflow:

``` bash
git status

git add .

git commit -m "Finalize Uber Eats ML capstone"

git switch main

git pull origin main

git merge feature/uber-eats-pipeline
```

Meaningful commits used during development include:

``` text
Initialize Uber Eats analytics project
Generate synthetic order data
Implement customer segmentation
Add NLP sentiment analysis
Implement delivery time prediction
Add demand forecasting
Finalize business insights
```

Before final submission:

``` bash
git status
```

should show a clean working tree after all intended changes have been
committed.

------------------------------------------------------------------------

# 24. Final Presentation Structure

The final 15--20 minute presentation should follow the project journey.

## 1. Business Problem

Explain what the platform is trying to improve:

-   Customer experience
-   Restaurant performance
-   Delivery reliability
-   Operational planning

## 2. Dataset

Explain:

-   Dataset sources/generation
-   Tables
-   Key fields
-   Dataset size
-   Time period

## 3. Data Preparation

Explain:

-   Missing values
-   Duplicates
-   Validation
-   Cleaning
-   Feature engineering

## 4. Segmentation

Explain:

-   K-Means
-   DBSCAN
-   PCA
-   Cluster interpretation

## 5. NLP

Explain:

-   Text preprocessing
-   TF-IDF
-   Naive Bayes
-   VADER
-   Complaint themes
-   Evaluation

## 6. Regression

Explain:

-   Target
-   Features
-   Linear Regression
-   Ridge
-   Lasso
-   Random Forest
-   MAE/RMSE/R²
-   Feature importance
-   Best model

## 7. Forecasting

Explain:

-   Hourly aggregation
-   Demand patterns
-   Decomposition
-   ADF
-   ARIMA
-   Prophet
-   Chronological validation
-   MAE/RMSE/MAPE
-   Best model

## 8. Business Impact

Connect technical results to operational actions.

## 9. Limitations

Be transparent about synthetic data, limited history, model assumptions,
and evaluation limitations.

## 10. Future Scope

Explain how the solution could be improved for production.

------------------------------------------------------------------------

# 25. Final Business Recommendations

Based on the completed analysis:

### Recommendation 1 -- Reduce Delivery Delays

Delivery delays were the largest complaint theme at **33.39%**.

Prioritize delivery-time reduction initiatives and connect them to the
delivery prediction model.

### Recommendation 2 -- Improve Food Freshness

Food quality/freshness represented **32.94%** of complaint themes.

Restaurants with long preparation times should receive operational
attention because preparation time was one of the strongest
delivery-time predictors.

### Recommendation 3 -- Focus on Distance and Preparation Time

The Random Forest feature analysis identified delivery distance and
preparation time as the two strongest features.

Operational planning should therefore prioritize:

``` text
Restaurant preparation
        +
Delivery-zone/routing optimization
        +
Driver dispatch
```

### Recommendation 4 -- Use Forecasts for Capacity Planning

Use the preferred demand forecast to anticipate hourly demand and adjust
rider/restaurant capacity accordingly.

Capacity should be increased when forecasted demand exceeds operational
thresholds.

### Recommendation 5 -- Target Customer Segments

Use customer segmentation to differentiate high-value customers from
lower-frequency groups.

Retention resources should be concentrated on customers with high
spending, high order frequency, and strong engagement.

### Recommendation 6 -- Monitor Restaurant Clusters

Restaurant clusters can be used to identify groups requiring:

-   Operational support
-   Quality improvement
-   Delivery improvement
-   Cancellation reduction

------------------------------------------------------------------------

# 26. Overall Capstone Outcome

The UberEats ML Capstone demonstrates a complete machine-learning
workflow:

``` text
Business Problem
      ↓
Data Generation
      ↓
Data Validation
      ↓
EDA
      ↓
Feature Engineering
      ↓
Unsupervised Learning
      ↓
NLP
      ↓
Supervised Regression
      ↓
Time-Series Forecasting
      ↓
Model Evaluation
      ↓
Business Insights
      ↓
Recommendations
      ↓
Reproducible Git Project
```

The most important outcome is not a single model. It is the ability to
connect multiple analytical techniques into a coherent decision-support
system.

The completed project demonstrates:

-   **Segmentation** for understanding customers and restaurants
-   **NLP** for understanding customer feedback
-   **Regression** for estimating delivery time
-   **Forecasting** for planning future demand
-   **Model evaluation** for selecting appropriate approaches
-   **Business interpretation** for turning predictions into actions

------------------------------------------------------------------------

## 27. Final Deliverable Checklist

Before submission, verify that the repository contains:

-   [ ] Git repository
-   [ ] Synthetic datasets
-   [ ] Data dictionary
-   [ ] Data-cleaning pipeline
-   [ ] EDA notebook
-   [ ] K-Means implementation
-   [ ] DBSCAN implementation
-   [ ] PCA analysis
-   [ ] NLP preprocessing pipeline
-   [ ] TF-IDF implementation
-   [ ] Sentiment classification model
-   [ ] Regression models
-   [ ] Regression model comparison
-   [ ] Feature importance analysis
-   [ ] Actual vs predicted visualization
-   [ ] ARIMA model
-   [ ] Prophet model
-   [ ] Forecast comparison
-   [ ] Forecast visualizations
-   [ ] Business insights
-   [ ] Business recommendations
-   [ ] Model limitations
-   [ ] Future improvement opportunities
-   [ ] Saved model artifacts
-   [ ] Processed datasets
-   [ ] Output/evaluation files
-   [ ] Final presentation
-   [ ] README/documentation

------------------------------------------------------------------------

## 28. Conclusion

The UberEats ML Capstone brings together multiple machine-learning
disciplines into one end-to-end analytical solution.

The project shows how a food-delivery platform can move from raw
transactional and customer-feedback data to:

**customer understanding → operational prediction → demand planning →
business action.**

The strongest demonstrated technical outcomes are:

-   **Ridge Regression** for delivery-time prediction, with
    approximately **4.03 minutes MAE**, **5.03 minutes RMSE**, and
    **0.945 R²**.
-   **Prophet** for hourly demand forecasting, with approximately **1.59
    orders MAE**, **2.02 orders RMSE**, and **48.15% MAPE** on the
    chronological test set.
-   **VADER** providing substantially stronger broad-review sentiment
    performance than the small template-based supervised sentiment
    evaluation.
-   **Delivery delays and food quality/freshness** emerging as the two
    largest complaint themes.
-   **Delivery distance and preparation time** emerging as the strongest
    operational predictors in the delivery-time feature analysis.

The final solution is intended as a capstone demonstration and a
foundation for a production-grade ML system with richer real-world data,
stronger validation, monitoring, and deployment infrastructure.
