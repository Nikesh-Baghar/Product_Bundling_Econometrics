
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.stattools import adfuller, kpss, coint
import statsmodels.api as sm
from scipy.stats import zscore

# Helper function to load the data
@st.cache_data
def load_data():
    df_order = pd.read_csv("2_orders.csv")
    df_order_prior = pd.read_csv("2_order_products__prior.csv")
    df_order_train = pd.read_csv("2_order_products__train.csv")
    df_product = pd.read_csv("2_products.csv")
    df_department = pd.read_csv("2_departments.csv")
    df_aisles = pd.read_csv("2_aisles.csv")
    return df_order, df_order_prior, df_order_train, df_product, df_department, df_aisles

# Data load
df_order, df_order_prior, df_order_train, df_product, df_department, df_aisles = load_data()

# Data Preprocessing and Analysis
df_order["days_since_prior_order"].fillna(0, inplace=True)
df_order['cum_days'] = df_order.groupby('user_id')['days_since_prior_order'].cumsum()
df_order['week_no'] = (df_order['cum_days'] // 7 + 1).astype(int)

df_product_merge = df_product.merge(df_department, on='department_id', how='left')
df_order_prior_merge = df_order_prior.merge(df_product_merge[['product_id', 'department']], on='product_id', how='left')
df_order_prior_merge = df_order_prior_merge.merge(df_order[['order_id', 'order_number', 'user_id', 'week_no']], on='order_id', how='left')

# Weekly Sales Calculation
df_order_prior_merge['global_week'] = df_order_prior_merge['week_no']
df_order_prior_merge = df_order_prior_merge.drop_duplicates(subset=['global_week', 'department', 'order_id'])
weekly_sales = df_order_prior_merge.groupby(['global_week', 'department']).size().reset_index(name='units_sold').pivot(index='global_week', columns='department', values='units_sold').fillna(0)
weekly_sales_log = np.log1p(weekly_sales)

# Correlation Heatmap
st.title("Cointegration and Bundling Analysis")
st.subheader("Correlation Heatmap of Product Category Sales")
corr_matrix = weekly_sales_log.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='Spectral_r', square=True, linewidths=0.5)
plt.title("Correlation Heatmap of Product Category Sales (Weekly)")
plt.tight_layout()
st.pyplot()

# Cointegration Testing
st.subheader("Cointegration Testing: ADF and KPSS")
adf_results = []
kpss_results = []

for col in weekly_sales_log.columns:
    series = weekly_sales_log[col].dropna()
    adf_stat, adf_p, *_ = adfuller(series, autolag='AIC')
    adf_results.append({'department': col, 'adf_stat': adf_stat, 'adf_pvalue': adf_p})
    kpss_stat, kpss_p, *_ = kpss(series, regression='c')
    kpss_results.append({'department': col, 'kpss_stat': kpss_stat, 'kpss_pvalue': kpss_p})

adf_df = pd.DataFrame(adf_results)
kpss_df = pd.DataFrame(kpss_results)

st.write("ADF Test Results:", adf_df)
st.write("KPSS Test Results:", kpss_df)

# Bundling Signal Detection
st.subheader("Bundling Signal Detection Based on Cointegration")
bundling_signals = {}
for idx, row in adf_df.iterrows():
    indep = row['department']
    dep = row['department']
    X = sm.add_constant(weekly_sales_log[indep])
    y = weekly_sales_log[dep]
    model = sm.OLS(y, X).fit()
    spread = model.resid
    z_scores = zscore(spread)

    signal_weeks = weekly_sales_log.index[z_scores < -1.5].tolist()
    signal_zs = z_scores[z_scores < -1.5]

    if len(signal_weeks) > 0:
        bundling_signals[f"{dep} ~ {indep}"] = list(zip(signal_weeks, signal_zs))
        for week, z in zip(signal_weeks, signal_zs):
            st.write(f"Week {week}: z = {z:.2f} → Suggest bundling '{dep}' with '{indep}'")

# Allow user to select product pairs for bundling
st.subheader("Select Product Pair for Detailed Analysis")
pairs = list(bundling_signals.keys())
selected_pair = st.selectbox("Choose a Product Pair", pairs)
if selected_pair:
    st.write(f"Bundling Signal for {selected_pair}:")
    signal_data = bundling_signals[selected_pair]
    st.write(signal_data)
