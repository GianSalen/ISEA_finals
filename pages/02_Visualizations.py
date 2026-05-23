"""
Visualizations Page
Create and explore interactive data visualizations
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(
    page_title="Visualizations - ISEA Dashboard",
    page_icon="📈",
    layout="wide",
)

st.title("📊 Visualizations")
st.markdown("*Create and explore interactive data visualizations*")
st.markdown("---")

# Sidebar controls
st.sidebar.subheader("📋 Visualization Settings")

with st.sidebar:
    viz_type = st.selectbox(
        "Select Visualization Type",
        ["Line Chart", "Bar Chart", "Scatter Plot", "Pie Chart", "Heatmap"]
    )
    
    st.markdown("---")
    
    st.write("**Data Source**: Ready to connect")
    st.info("Load your data from the `/data/` folder to create visualizations.")

# Main content area
st.subheader("📈 Visualization Creator")

# Tabs for different sections
tab1, tab2, tab3 = st.tabs(["Create Chart", "Gallery", "Settings"])

with tab1:
    st.write("### Create Your Visualization")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Step 1: Select Data Source**")
        data_source = st.selectbox(
            "Choose dataset",
            ["No datasets loaded", "Upload new dataset"],
            key="data_source"
        )
    
    with col2:
        st.write("**Step 2: Choose Variables**")
        st.info("Load data to select variables for visualization")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Step 3: Chart Configuration**")
        chart_type = st.radio(
            "Chart Type",
            ["Line", "Bar", "Scatter", "Pie", "Box Plot"],
            horizontal=True
        )
    
    with col2:
        st.write("**Step 4: Apply Filters**")
        st.multiselect(
            "Filter options",
            ["Option 1", "Option 2", "Option 3"],
            disabled=True
        )
    
    st.markdown("---")
    st.button("📊 Generate Visualization", use_container_width=True)
    
    # Placeholder for chart
    st.info("Load your data and configure the chart to generate visualization")

with tab2:
    st.write("### Visualization Gallery")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Sample Visualizations")
        st.write("Examples of different chart types and configurations")
        st.info("Charts will appear here once data is loaded")
    
    with col2:
        st.markdown("#### Recent Charts")
        st.write("Your recently created visualizations")
        st.info("No visualizations created yet")

with tab3:
    st.write("### Advanced Settings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Display Options")
        show_legend = st.checkbox("Show Legend", value=True)
        show_grid = st.checkbox("Show Grid", value=True)
        animation = st.checkbox("Enable Animation", value=False)
    
    with col2:
        st.subheader("Color & Style")
        color_scheme = st.selectbox(
            "Color Scheme",
            ["Default", "Pastel", "Bold", "Dark", "Light"]
        )
        chart_style = st.selectbox(
            "Chart Style",
            ["Standard", "Minimal", "Detailed"]
        )

st.markdown("---")

# Quick reference section
with st.expander("📚 Visualization Types Reference"):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Line Chart**
        - Best for: Time series, trends
        - Use case: Stock prices, metrics over time
        """)
    
    with col2:
        st.markdown("""
        **Bar Chart**
        - Best for: Comparisons, categories
        - Use case: Sales by region, category counts
        """)
    
    with col3:
        st.markdown("""
        **Scatter Plot**
        - Best for: Correlations, distribution
        - Use case: Price vs rating, two-variable analysis
        """)
