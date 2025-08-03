📦 Detecting Bundling Opportunities Using Cointegration and Revenue Impact Simulation
🧠 Topic    
This project leverages time-series econometric techniques to identify product category pairs that exhibit long-term co-movement (cointegration) and simulates the revenue impact of implementing a bundling strategy. The approach combines business insights with statistical modeling to inform marketing or pricing strategies in e-commerce or retail.

🎯 Objectives
Identify Cointegrated Product Category Pairs
Use Engle-Granger cointegration tests to detect categories that consistently move together over time, suggesting natural bundling opportunities.

Estimate Long-Run Relationships
Use OLS regression to quantify the relationship (slope ratio) between sales of the cointegrated pairs, forming the basis of a potential bundle.

Detect Bundling Opportunities Using Z-Score Spreads
Track deviations from the long-run relationship using z-scores to find windows of opportunity where one category underperforms—ideal moments to push a bundle.

Simulate Revenue Uplift from Bundling Strategy
Simulate increased sales (e.g., +5% uplift) during bundling weeks and use paired t-tests to determine if the uplift is statistically significant.


💼 Business Implications
Strategic Bundling:
Businesses can use statistical evidence to identify which products are naturally consumed together and offer bundled pricing to boost underperforming items.

Timing Promotions:
Bundling based on z-score signals ensures promotions are launched when they’re most likely to succeed, avoiding constant discounts.

Revenue Forecasting:
The simulated model helps estimate revenue gains before implementation, aiding marketing teams in decision-making.


🛠️ Techniques Used
Data Preprocessing

Merging multiple CSVs containing order, product, department, and aisle data.

Creating user-level cumulative week indicators.

Econometric Modeling

Engle-Granger cointegration test (ADF and KPSS on residuals).

Error Correction Model (ECM)

Ordinary Least Squares (OLS) regression.

Statistical Analysis

Z-score calculations to identify divergence from equilibrium.

Paired t-test for assessing uplift significance.

Visualization

Matplotlib and Seaborn for plotting sales trends and z-score spreads.



📊 Interpretation of Output
Cointegration Results:
23 category pairs were found to be cointegrated, e.g., Canned Vegetables & Pasta Sauce, implying stable long-run demand patterns.

OLS Regression Slopes:
Slope values (e.g., 0.89) indicate the long-run proportional sales ratio between two categories. This helps define a bundle. 
Z-Score Spread Signals:
When the z-score of residuals deviates significantly (e.g., |z| > 1.5), it suggests that one category is underperforming relative to the other, signaling a good bundling week.

Simulated Uplift:
Hypothetically adding a 5% uplift during signal weeks resulted in a statistically significant increase in weekly sales (p-value < 0.05 from paired t-test).

Customer Retention & Cross-Sell:
Properly timed bundles can improve cart value and introduce users to complementary categories, potentially increasing LTV
