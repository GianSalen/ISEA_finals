"""
Gian Roilo P. Salen
ISEA Finals 2026
Data Dashboard App
"""

import streamlit as st
from pathlib import Path

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="ISEA Finals Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================================
# CUSTOM STYLING
# ============================================================================

st.markdown("""
<style>
    /* Main container styling */
    .main {
        padding-top: 2rem;
    }
    
    /* Header styling */
    h1 {
        color: #1f77b4;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    h2 {
        color: #2c3e50;
        font-weight: 600;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #1f77b4;
        padding-bottom: 0.5rem;
    }
    
    /* Card styling */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Sidebar styling */
    .sidebar .sidebar-content {
        padding: 2rem 1rem;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #1f77b4;
        color: white;
        font-weight: 600;
        border-radius: 5px;
        border: none;
        padding: 0.5rem 1.5rem;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #1557a0;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(31, 119, 180, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# SIDEBAR
# ============================================================================

with st.sidebar:
    st.title("🎯 Navigation")
    st.markdown("---")
    st.markdown("""
    **Project**: ISEA Finals 2026  
    **Author**: Gian Roilo P. Salen  
    **Type**: Data Dashboard
    """)
    st.markdown("---")

# ============================================================================
# MAIN HOME PAGE CONTENT
# ============================================================================

st.title("📊 ISEA Finals Dashboard")
st.markdown("*Welcome to your comprehensive data analysis and visualization platform*")
st.markdown("---")

# Overview section
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="📈 Total Datasets",
        value="—",
        delta="Ready to explore",
        delta_color="off"
    )

with col2:
    st.metric(
        label="📉 Visualizations",
        value="—",
        delta="Custom analytics",
        delta_color="off"
    )

with col3:
    st.metric(
        label="🔍 Data Explorer",
        value="—",
        delta="Full dataset view",
        delta_color="off"
    )

st.markdown("---")

# Features overview
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏠 Home")
    st.write("""
    Get started with an overview of your dashboard capabilities.
    Access quick statistics and navigation to all features.
    """)

with col2:
    st.subheader("📊 Visualizations")
    st.write("""
    Create and explore custom data visualizations.
    Analyze trends, patterns, and insights with interactive charts.
    """)

with col1:
    st.subheader("🔎 Dataset Explorer")
    st.write("""
    Browse and explore your datasets in detail.
    Filter, search, and understand your data structure.
    """)

with col2:
    st.subheader("⚙️ Features")
    st.write("""
    - Interactive visualizations
    - Real-time data exploration
    - Professional styling
    - Multi-page navigation
    - Responsive design
    """)

st.markdown("---")

# Getting started section
st.subheader("🚀 Getting Started")
st.info("""
👈 Use the sidebar or the page navigation to explore the dashboard.
Select **Visualizations** to create custom charts or **Dataset Explorer** to browse your data.
""")

st.markdown("---")

# Footer
st.markdown("""
<div style="text-align: center; color: #7f8c8d; font-size: 0.9rem; margin-top: 3rem;">
    <p>ISEA Finals 2026 | Data Dashboard | Built with Streamlit</p>
</div>
""", unsafe_allow_html=True) 
