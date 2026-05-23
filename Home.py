
# Gian Roilo P. Salen
# ISEA Finals 2026
# Data Dashboard App


# Home Page
# Comparative Analysis of Major Philippine Companies

import streamlit as st

st.set_page_config(
    page_title="Comparative Analysis - ISEA Dashboard",
    page_icon="📊",
    layout="wide",
)

st.title("Comparative Analysis of Major Philippine Companies")
st.markdown("*Historical stock data analysis from investing.com*")
st.markdown("---")

# Dataset Overview
st.subheader("Dataset Overview")
st.markdown("""
This analysis includes historical stock data from **investing.com** for five major Philippine companies:

- **SM Investments Corporation** (SM)
- **BDO Unibank, Inc.** (BDO)
- **Manila Electric Company** (Meralco)
- **Bank of the Philippine Islands** (BPI)
- **Jollibee Foods Corporation** (Jollibee)
""")

st.markdown("---")

# Data Structure
st.subheader("Data Structure")

st.markdown("*The five separate CSV files have been merged into a single unified dataset for comparative analysis.*")

col1, col2 = st.columns([1, 1.4])

with col1:
    st.markdown("""
    **Original Columns** (from investing.com):
    - Date
    - Price
    - Open
    - High
    - Low
    - Vol.
    - Change %
    """)

with col2:
    st.markdown("""
    **Merged Dataset Columns**:
    - **Date**: Trading date
    - **Price**: Closing price
    - **Open**: Opening price
    - **High**: Highest price of the day
    - **Low**: Lowest price of the day
    - **Volume**: Trading volume (standardized from Vol.)
    - **Change_pct**: Percentage change (standardized from Change %)
    - **Company**: Company identifier (SM, BDO, Meralco, BPI, or Jollibee)
    """)

st.markdown("---")

# About the Pages
st.subheader("About the Pages")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **Visualizations Tab**
    
    The Visualizations page contains the analysis, interactive graphs, and charts. 
    Explore trends, patterns, and comparisons between the five major Philippine companies' stock performance.
    """)

with col2:
    st.markdown("""
    **Data Explorer Page**
    
    The Data Explorer allows you to upload your own downloaded data from investing.com to have it displayed here. 
    You can also compare multiple datasets you've uploaded to identify patterns and trends across different time periods or additional companies.
    """)

col1, col2 = st.columns(2)
with col1:
    if st.button("📊 View Visualizations", use_container_width=True):
        st.switch_page("pages/02_Visualizations.py")

with col2:
    if st.button("🔍 Explore Dataset", use_container_width=True):
        st.switch_page("pages/03_Dataset_Explorer.py")

st.markdown("---")

# References
st.subheader("References")
st.markdown("""
Data sourced from investing.com:

- [Bank of the Philippine Islands (BPI) Historical Data](https://www.investing.com/equities/bk-of-phi-isla-historical-data)
- [Jollibee Foods Corporation Historical Data](https://www.investing.com/equities/jollibee-foods-historical-data)
- [Manila Electric Company (Meralco) Historical Data](https://www.investing.com/equities/manila-electri-historical-data)
- [BDO Unibank, Inc. Historical Data](https://www.investing.com/equities/bdo-unibank-historical-data)
- [SM Investments Corporation Historical Data](https://www.investing.com/equities/sm-investment-historical-data)
""")
