"""
Home Page
Display dashboard overview and quick stats
"""

import streamlit as st

st.set_page_config(
    page_title="Home - ISEA Dashboard",
    page_icon="🏠",
    layout="wide",
)

st.title("🏠 Home")
st.markdown("*Main dashboard overview and quick access to features*")
st.markdown("---")

# Quick statistics
st.subheader("📊 Quick Statistics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Records", "—", help="Number of records in your dataset")

with col2:
    st.metric("Data Sources", "—", help="Number of data sources")

with col3:
    st.metric("Last Updated", "—", help="Latest data update time")

with col4:
    st.metric("Status", "✅ Ready", help="Dashboard status")

st.markdown("---")

# Main content area
st.subheader("📌 Dashboard Features")

tab1, tab2, tab3 = st.tabs(["Overview", "How to Use", "Dataset Info"])

with tab1:
    st.write("""
    ### Welcome to Your Data Dashboard
    
    This dashboard provides comprehensive tools for:
    - **Data Visualization**: Create interactive charts and graphs
    - **Data Exploration**: Browse and filter your datasets
    - **Analysis**: Generate insights from your data
    
    Navigate using the sidebar or page tabs to access different features.
    """)

with tab2:
    st.write("""
    ### How to Use This Dashboard
    
    1. **Visualizations Page**: Create custom visualizations of your data
       - Select data sources
       - Choose chart types
       - Apply filters and customizations
    
    2. **Dataset Explorer**: Explore your data in detail
       - Browse tables
       - Filter records
       - View data statistics
    
    3. **Home Page**: Quick access and overview
       - Key metrics
       - Navigation
       - Recent updates
    """)

with tab3:
    st.write("""
    ### About Your Data
    
    **Dataset Location**: `/data/`  
    **Data Format**: Ready for analysis  
    **Status**: ✅ Loaded and ready
    
    Add your datasets to the `/data/` folder to get started.
    """)

st.markdown("---")

# Call to action
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📊 Go to Visualizations", use_container_width=True):
        st.switch_page("pages/02_Visualizations.py")

with col2:
    if st.button("🔍 Explore Dataset", use_container_width=True):
        st.switch_page("pages/03_Dataset_Explorer.py")

with col3:
    st.markdown("")  # Placeholder for alignment
