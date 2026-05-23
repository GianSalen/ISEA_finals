# Dataset Explorer Page

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Conversion functions for investing.com data
def convert_volume(volume_str):
    # Convert volume strings like '1.5M', '800.4K', '1B' to actual numbers
    if pd.isna(volume_str) or volume_str == '—' or volume_str == '':
        return 0
    
    volume_str = str(volume_str).strip()
    multipliers = {'K': 1000, 'M': 1000000, 'B': 1000000000}
    
    for suffix, multiplier in multipliers.items():
        if suffix in volume_str:
            try:
                return float(volume_str.replace(suffix, '')) * multiplier
            except:
                return 0
    
    try:
        return float(volume_str)
    except:
        return 0

def convert_change_percentage(change_str):
    # Convert change percentage strings like '2.5%', '-1.2%' to actual numbers
    if pd.isna(change_str) or change_str == '':
        return 0
    
    change_str = str(change_str).strip().replace('%', '')
    try:
        return float(change_str)
    except:
        return 0

def process_investing_data(df):
    df_processed = df.copy()
    
    # Convert Date column to datetime
    if 'Date' in df_processed.columns:
        df_processed['Date'] = pd.to_datetime(df_processed['Date'], format='%m/%d/%Y', errors='coerce')
    
    # Convert numeric columns
    numeric_cols = ['Price', 'Open', 'High', 'Low']
    for col in numeric_cols:
        if col in df_processed.columns:
            df_processed[col] = pd.to_numeric(df_processed[col], errors='coerce')
    
    # Convert Volume
    if 'Vol.' in df_processed.columns:
        df_processed['Vol.'] = df_processed['Vol.'].apply(convert_volume)
    
    # Convert Change %
    if 'Change %' in df_processed.columns:
        df_processed['Change %'] = df_processed['Change %'].apply(convert_change_percentage)
    
    # Sort by date
    if 'Date' in df_processed.columns:
        df_processed = df_processed.sort_values('Date')
    
    return df_processed

st.set_page_config(
    page_title="Dataset Explorer - ISEA Dashboard",
    page_icon="🔍",
    layout="wide",
)

st.title("Dataset Explorer")
st.markdown("*Browse and explore your datasets in detail*")
st.markdown("---")

# Sidebar controls
st.sidebar.subheader("Explorer Controls")

# Initialize session state for uploaded data
if 'uploaded_data' not in st.session_state:
    st.session_state.uploaded_data = None

# Data upload section - moved to sidebar
with st.sidebar:
    st.markdown("### 📁 Upload Data")
    uploaded_file = st.file_uploader(
        "Upload historical data from Investing.com",
        type=["csv"],
        help="Upload CSV file with columns: Date, Price, Open, High, Low, Vol., Change %"
    )
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            
            # Validate columns
            required_cols = ['Date', 'Price', 'Open', 'High', 'Low', 'Vol.', 'Change %']
            missing_cols = [col for col in required_cols if col not in df.columns]
            
            if missing_cols:
                st.error(f"Missing columns: {', '.join(missing_cols)}")
                st.info(f"Expected columns: {', '.join(required_cols)}")
            else:
                # Process the data
                df_processed = process_investing_data(df)
                st.session_state.uploaded_data = df_processed
                st.success("✅ Data uploaded and processed successfully!")
                st.balloons()
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")

# Main content area
if st.session_state.uploaded_data is not None:
    df = st.session_state.uploaded_data
    
    # Overview metrics
    st.subheader("Data Overview")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Total Records", len(df))
    with col2:
        st.metric("Date Range", f"{df['Date'].min().strftime('%m/%d/%Y')} - {df['Date'].max().strftime('%m/%d/%Y')}")
    with col3:
        st.metric("Avg Price", f"${df['Price'].mean():.2f}")
    with col4:
        st.metric("Avg Volume", f"{df['Vol.'].mean():.0f}")
    with col5:
        st.metric("Avg Change %", f"{df['Change %'].mean():.2f}%")
    
    st.markdown("---")
    
    # Tabs for different views
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Price Chart", "📊 Statistics", "📋 Data Table", "📉 Advanced Analytics"])
    
    with tab1:
        st.subheader("Price Trend Over Time")
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df['Date'], y=df['Price'],
            mode='lines+markers',
            name='Price',
            line=dict(color='#1f77b4', width=2),
            hovertemplate='<b>%{x|%m/%d/%Y}</b><br>Price: $%{y:.2f}<extra></extra>'
        ))
        
        fig.update_layout(
            title="Historical Price Data",
            xaxis_title="Date",
            yaxis_title="Price ($)",
            hovermode='x unified',
            template='plotly_white',
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Open, High, Low, Close comparison
        st.subheader("OHLC Comparison")
        
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=df['Date'], y=df['Open'], name='Open', line=dict(color='green')))
        fig2.add_trace(go.Scatter(x=df['Date'], y=df['High'], name='High', line=dict(color='blue')))
        fig2.add_trace(go.Scatter(x=df['Date'], y=df['Low'], name='Low', line=dict(color='red')))
        fig2.add_trace(go.Scatter(x=df['Date'], y=df['Price'], name='Price', line=dict(color='black', width=2)))
        
        fig2.update_layout(
            title="Open, High, Low, Price Comparison",
            xaxis_title="Date",
            yaxis_title="Price ($)",
            hovermode='x unified',
            template='plotly_white',
            height=500
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    with tab2:
        st.subheader("Statistical Summary")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Price Statistics**")
            price_stats = pd.DataFrame({
                "Metric": ["Min", "Max", "Mean", "Median", "Std Dev"],
                "Value": [
                    f"${df['Price'].min():.2f}",
                    f"${df['Price'].max():.2f}",
                    f"${df['Price'].mean():.2f}",
                    f"${df['Price'].median():.2f}",
                    f"${df['Price'].std():.2f}"
                ]
            })
            st.dataframe(price_stats, use_container_width=True, hide_index=True)
        
        with col2:
            st.write("**Volume Statistics**")
            vol_stats = pd.DataFrame({
                "Metric": ["Min", "Max", "Mean", "Median", "Std Dev"],
                "Value": [
                    f"{df['Vol.'].min():.0f}",
                    f"{df['Vol.'].max():.0f}",
                    f"{df['Vol.'].mean():.0f}",
                    f"{df['Vol.'].median():.0f}",
                    f"{df['Vol.'].std():.0f}"
                ]
            })
            st.dataframe(vol_stats, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Change % Statistics**")
            change_stats = pd.DataFrame({
                "Metric": ["Min", "Max", "Mean", "Median", "Std Dev"],
                "Value": [
                    f"{df['Change %'].min():.2f}%",
                    f"{df['Change %'].max():.2f}%",
                    f"{df['Change %'].mean():.2f}%",
                    f"{df['Change %'].median():.2f}%",
                    f"{df['Change %'].std():.2f}%"
                ]
            })
            st.dataframe(change_stats, use_container_width=True, hide_index=True)
        
        with col2:
            st.write("**Data Quality**")
            quality = pd.DataFrame({
                "Column": ["Date", "Price", "Open", "High", "Low", "Vol.", "Change %"],
                "Non-Null": [
                    df['Date'].notna().sum(),
                    df['Price'].notna().sum(),
                    df['Open'].notna().sum(),
                    df['High'].notna().sum(),
                    df['Low'].notna().sum(),
                    df['Vol.'].notna().sum(),
                    df['Change %'].notna().sum()
                ],
                "Missing": [
                    df['Date'].isna().sum(),
                    df['Price'].isna().sum(),
                    df['Open'].isna().sum(),
                    df['High'].isna().sum(),
                    df['Low'].isna().sum(),
                    df['Vol.'].isna().sum(),
                    df['Change %'].isna().sum()
                ]
            })
            st.dataframe(quality, use_container_width=True, hide_index=True)
    
    with tab3:
        st.subheader("Data Table")
        
        # Display dataframe with formatting
        display_df = df.copy()
        display_df['Date'] = display_df['Date'].dt.strftime('%m/%d/%Y')
        display_df['Price'] = display_df['Price'].apply(lambda x: f"${x:.2f}" if pd.notna(x) else "—")
        display_df['Open'] = display_df['Open'].apply(lambda x: f"${x:.2f}" if pd.notna(x) else "—")
        display_df['High'] = display_df['High'].apply(lambda x: f"${x:.2f}" if pd.notna(x) else "—")
        display_df['Low'] = display_df['Low'].apply(lambda x: f"${x:.2f}" if pd.notna(x) else "—")
        display_df['Vol.'] = display_df['Vol.'].apply(lambda x: f"{x:,.0f}" if pd.notna(x) else "—")
        display_df['Change %'] = display_df['Change %'].apply(lambda x: f"{x:.2f}%" if pd.notna(x) else "—")
        
        st.dataframe(display_df, use_container_width=True, height=600)
        
        # Download button
        csv = df.to_csv(index=False)
        st.download_button(
            label="📥 Download Processed Data (CSV)",
            data=csv,
            file_name=f"processed_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )
    
    with tab4:
        st.subheader("Advanced Analytics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Volume Over Time**")
            fig_vol = go.Figure()
            fig_vol.add_trace(go.Bar(
                x=df['Date'],
                y=df['Vol.'],
                name='Volume',
                marker=dict(color='#2ca02c'),
                hovertemplate='<b>%{x|%m/%d/%Y}</b><br>Volume: %{y:,.0f}<extra></extra>'
            ))
            fig_vol.update_layout(
                xaxis_title="Date",
                yaxis_title="Volume",
                hovermode='x unified',
                template='plotly_white',
                height=400
            )
            st.plotly_chart(fig_vol, use_container_width=True)
        
        with col2:
            st.write("**Change %**")
            fig_change = go.Figure()
            colors = ['red' if x < 0 else 'green' for x in df['Change %']]
            fig_change.add_trace(go.Bar(
                x=df['Date'],
                y=df['Change %'],
                name='Change %',
                marker=dict(color=colors),
                hovertemplate='<b>%{x|%m/%d/%Y}</b><br>Change: %{y:.2f}%<extra></extra>'
            ))
            fig_change.update_layout(
                xaxis_title="Date",
                yaxis_title="Change %",
                hovermode='x unified',
                template='plotly_white',
                height=400
            )
            st.plotly_chart(fig_change, use_container_width=True)
        
        # Price distribution
        st.write("**Price Distribution**")
        fig_dist = px.histogram(df, x='Price', nbins=30, title="Price Distribution",
                               labels={'Price': 'Price ($)', 'count': 'Frequency'})
        fig_dist.update_layout(template='plotly_white', height=400)
        st.plotly_chart(fig_dist, use_container_width=True)

else:
    # No data uploaded yet
    st.subheader("Data Overview")
    
    st.info("""
    ### 📂 Welcome to Dataset Explorer!
    
    **To get started:**
    1. Click the upload button in the sidebar
    2. Select a CSV file from Investing.com with the following columns:
       - **Date**: Date in MM/DD/YYYY format
       - **Price**: Stock price
       - **Open**: Opening price
       - **High**: Highest price
       - **Low**: Lowest price
       - **Vol.**: Trading volume (e.g., 1.5M, 800.4K, 1B)
       - **Change %**: Change percentage (e.g., 2.5%, -1.2%)
    
    3. After uploading, you'll see:
       - Price trends and OHLC charts
       - Statistical summaries
       - Complete data table
       - Advanced analytics with volume and change patterns
    """)
    
    # Show example of expected data format
    st.subheader("Expected Data Format")
    st.markdown("*The default format from investing.com historical data*")
    example_data = pd.DataFrame({
        'Date': ['01/15/2024', '01/14/2024', '01/13/2024'],
        'Price': [150.25, 149.50, 151.75],
        'Open': [149.00, 150.25, 149.50],
        'High': [151.00, 151.50, 152.00],
        'Low': [148.50, 149.00, 149.25],
        'Vol.': ['2.5M', '1.8M', '3.2M'],
        'Change %': ['1.5%', '-1.5%', '1.5%']
    })
    st.dataframe(example_data, use_container_width=True, hide_index=True)
