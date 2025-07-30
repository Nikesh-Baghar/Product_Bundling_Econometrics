# Product_Bundling_Opportunity
Detecting Bundling Opportunities Using Cointegration and Revenue Impact Simulation
This project demonstrates a methodology for identifying product bundling opportunities using cointegration analysis and simulating the revenue impact of such a strategy. The project focuses on uncovering long-run relationships between product categories and leveraging deviations from these relationships to suggest optimal times for bundling, ultimately aiming to increase weekly sales.

Project Objectives:

Identify Cointegrated Product Category Pairs: Utilize Engle-Granger cointegration tests to discover product categories that exhibit long-term co-movement, making them suitable candidates for bundling.

Estimate Long-Run Relationships (OLS): For each cointegrated pair, fit Ordinary Least Squares (OLS) regression models to calculate bundle ratios (slope coefficients). These ratios guide the bundling of pairs, especially when sales of one category are underperforming.

Detect Bundling Opportunities Based on Z-Score Spreads: Continuously monitor deviations from established long-run trends using z-scores of residual spreads. This helps in identifying specific weeks where bundling could be beneficial (i.e., when one category shows signs of underperformance).

Simulate Revenue Uplift from Bundling Strategy: Apply a hypothetical sales uplift (e.g., 5%) to simulate the potential increase in revenue due to the bundling strategy. A paired t-test is then used to statistically evaluate whether the observed increase in weekly sales is a real effect of bundling or merely random variation.

Data
The analysis uses several CSV files, which are loaded into pandas DataFrames:

Data Consolidation and Preparation
The raw data undergoes several processing steps to prepare it for analysis:

Missing values in days_since_prior_order are filled with 0, treating the first order as the starting point for a user.

Cumulative days since the first order are calculated for each user.

Cumulative days are converted into week_no, starting from Week 1.

Department names are merged with product information.

Order line items are merged with product-department data.

Order-level metadata (including week_no) is appended to each product line.

A global_week index is created, assuming a common timeline for all users.

Weekly total units sold per department are aggregated and pivoted.

A log(1 + x) transformation is applied to stabilize variance and handle zero values, preparing the data for time series tests.

Irrelevant product categories ('missing', 'other') are dropped from the dataset.

The final processed DataFrame (weekly_sales_log) contains the log-transformed quantity sold for each product category per week, with a shape of (53, 19).

Methodology
The core of the methodology involves:

Preparation: Transforming raw sales data into weekly, log-transformed units per department, suitable for time series analysis.

Cointegration Testing: Applying the Engle-Granger test to identify pairs of product categories that have a stable, long-term relationship despite short-term fluctuations.

OLS Regression: Estimating the long-run equilibrium relationship between cointegrated pairs.

Z-Score Analysis: Monitoring the residuals from the OLS regression to identify when product sales deviate significantly from their long-run equilibrium, indicating bundling opportunities.

Revenue Simulation & Statistical Testing: Simulating the impact of bundling on revenue and using a paired t-test to determine the statistical significance of the observed revenue uplift.
