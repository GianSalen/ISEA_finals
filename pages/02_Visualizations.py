
# Visualizations Page

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

st.set_page_config(
    page_title="Visualizations - ISEA Dashboard",
    page_icon="📈",
    layout="wide",
)

st.title("Visualizations")
st.markdown("*Visual display of the top 5 stock performers of the Philippines*")
st.markdown("---")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/merged_cleaned_stocks.csv")
    
    # Convert numeric columns
    numeric_cols = ['Price', 'Open', 'High', 'Low', 'Volume', 'Change_pct']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

try:
    df = load_data()
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    
    companies = df['company'].unique().tolist()
    
    # Tabs for visualizations
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📈 Line Chart", 
        "🕯️ Candlestick", 
        "📊 Volume", 
        "📦 Boxplot", 
        "🔥 Heatmap"
    ])
    
    # Line Chart
    with tab1:
        st.subheader("Stock Price Over Time")
        st.markdown("**Purpose**: Trend analysis and compare growth across companies")
        
        selected_companies = st.multiselect(
            "Filter by company",
            companies,
            default=companies,
            key="line_chart_companies"
        )
        
        df_filtered = df[df['company'].isin(selected_companies)]
        
        fig = px.line(
            df_filtered,
            x='Date',
            y='Price',
            color='company',
            title='Stock Price Trends Over Time',
            labels={'Price': 'Price (PHP)', 'Date': 'Date'},
            hover_data={'Price': ':.2f'}
        )
        
        fig.update_layout(
            hovermode='x unified',
            height=500,
            template='plotly_white'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        **Insights:**
        - Jollibee, BDO, and BPI are slowly trending downwards
        - SM reached its peak in october 2024 but has strongly declined since
        - Meralco has had large and consistent growth 
        """)
    
    # Candlestick Chart
    with tab2:
        st.subheader("Candlestick Chart")
        st.markdown("**Purpose**: Detailed analysis of Open, High, Low, Close price movements")
        
        selected_company = st.selectbox(
            "Select company",
            companies,
            key="candlestick_company"
        )
        
        df_company = df[df['company'] == selected_company].copy()
        
        df_weekly = df_company.groupby('Date').agg({
            'Open': 'first',
            'High': 'max',
            'Low': 'min',
            'Price': 'last'
        }).reset_index()
        df_weekly.rename(columns={'Price': 'Close'}, inplace=True)
        
        fig = go.Figure(data=[go.Candlestick(
            x=df_weekly['Date'],
            open=df_weekly['Open'],
            high=df_weekly['High'],
            low=df_weekly['Low'],
            close=df_weekly['Close']
        )])
        
        fig.update_layout(
            title=f'Candlestick Chart - {selected_company}',
            yaxis_title='Price (PHP)',
            xaxis_title='Date',
            height=500,
            template='plotly_white',
            xaxis_rangeslider_visible=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        **Candlestick Interpretation:**
        - **Green candle**: Close > Open (bullish)
        - **Red candle**: Close < Open (bearish)
        - **Wick**: Shows High/Low price range
        """)
    
    # Volume Histogram
    with tab3:
        st.subheader("Trading Volume Distribution")
        st.markdown("**Purpose**: Identify which stocks are traded more actively")
        
        selected_companies_vol = st.multiselect(
            "Filter by company",
            companies,
            default=companies,
            key="volume_companies"
        )
        
        df_filtered_vol = df[df['company'].isin(selected_companies_vol)]
        
        fig = px.histogram(
            df_filtered_vol,
            x='Volume',
            color='company',
            barmode='group',
            title='Distribution of Trading Volume by company',
            labels={'Volume': 'Trading Volume', 'count': 'Frequency'},
            nbins=30
        )
        
        fig.update_layout(
            height=500,
            template='plotly_white',
            hovermode='x unified'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        **Key Insights:**
        - Banking Stocks Dominate Trading Activity
        - BPI and BDO have high trading volumes, and wide distributions
        - Meralco and SM Are Less Frequently Traded
        """)
    
    # Boxplot (Volatility)
    with tab4:
        st.subheader("Price Volatility by company")
        st.markdown("**Purpose**: Compare which stock is most volatile")
        
        selected_companies_volatility = st.multiselect(
            "Filter by company",
            companies,
            default=companies,
            key="volatility_companies"
        )
        
        df_filtered_volatility = df[df['company'].isin(selected_companies_volatility)]
        
        fig = px.box(
            df_filtered_volatility,
            x='company',
            y='Price',
            title='Price Distribution by company (Volatility Analysis)',
            labels={'Price': 'Price (PHP)', 'company': 'company'},
            points='outliers'
        )
        
        fig.update_layout(
            height=500,
            template='plotly_white'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Volatility statistics
        st.subheader("Volatility Metrics")
        
        volatility_stats = df_filtered_volatility.groupby('company')['Price'].agg([
            ('Mean Price', 'mean'),
            ('Std Dev', 'std'),
            ('Min', 'min'),
            ('Max', 'max'),
            ('Range', lambda x: x.max() - x.min())
        ]).round(2)
        
        st.dataframe(volatility_stats, use_container_width=True)
        
        st.markdown("""
        **Volatility Interpretation:**
        - **Higher Std Dev**: More volatile stock
        - **Wider range**: Greater price fluctuations
        - **Wider box**: More price variation in middle 50% of data
        """)
    
    # Correlation Heatmap
    with tab5:
        st.subheader("Correlation Heatmap")
        st.markdown("**Purpose**: Analyze price correlations between companies")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Create pivot table for correlation
            pivot_df = df.pivot_table(
                index='Date',
                columns='company',
                values='Price'
            ).ffill()
            
            correlation_matrix = pivot_df.corr()
            
            fig = px.imshow(
                correlation_matrix,
                text_auto='.2f',
                color_continuous_scale='RdBu_r',
                zmin=-1,
                zmax=1,
                title='Price Correlation Matrix Between Companies',
                labels={'color': 'Correlation'}
            )
            
            fig.update_layout(height=500)
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("**Correlation Strength:**")
            st.markdown("""
            - **+1.0**: Perfect positive correlation
            - **0.0**: No correlation
            - **-1.0**: Perfect negative correlation
            
            """)
        
        # Detailed correlation values
        st.subheader("Top Correlations")
        
        # Get top correlations (excluding diagonal)
        corr_pairs = []
        for i in range(len(correlation_matrix.columns)):
            for j in range(i+1, len(correlation_matrix.columns)):
                corr_pairs.append({
                    'company 1': correlation_matrix.columns[i],
                    'company 2': correlation_matrix.columns[j],
                    'Correlation': correlation_matrix.iloc[i, j]
                })
        
        corr_df = pd.DataFrame(corr_pairs).sort_values(
            'Correlation', 
            key=abs, 
            ascending=False
        )
        
        st.dataframe(corr_df, use_container_width=True)
    
    # SUMMARY STATISTICS SECTION
    st.markdown("---")
    st.subheader(" Summary Statistics")
    st.markdown("*Overall performance metrics and key statistics for each stock*")
    
    # Select companies for summary statistics
    selected_companies_summary = st.multiselect(
        "Select companies for summary statistics",
        companies,
        default=companies,
        key="summary_stats_companies"
    )
    
    if selected_companies_summary:
        df_summary = df[df['company'].isin(selected_companies_summary)].copy()
        
        # Create summary statistics table
        summary_stats = []
        
        for company in selected_companies_summary:
            df_company = df_summary[df_summary['company'] == company]
            
            if len(df_company) > 0:
                # Get first and last prices
                first_price = df_company.sort_values('Date').iloc[0]['Price']
                last_price = df_company.sort_values('Date').iloc[-1]['Price']
                
                # Calculate growth
                growth_amount = last_price - first_price
                growth_pct = (growth_amount / first_price * 100) if first_price != 0 else 0
                
                # Get price statistics
                highest_price = df_company['Price'].max()
                lowest_price = df_company['Price'].min()
                
                # Get volume statistics
                avg_volume = df_company['Volume'].mean()
                
                summary_stats.append({
                    'Company': company,
                    'Earliest Price': f"₱{first_price:.2f}",
                    'Current Price': f"₱{last_price:.2f}",
                    'Growth (₱)': f"₱{growth_amount:.2f}",
                    'Growth (%)': f"{growth_pct:.2f}%",
                    'Highest Price': f"₱{highest_price:.2f}",
                    'Lowest Price': f"₱{lowest_price:.2f}",
                    'Avg Volume': f"{avg_volume:,.0f}",
                    'Data Points': len(df_company)
                })
        
        summary_df = pd.DataFrame(summary_stats)
        st.dataframe(summary_df, use_container_width=True, hide_index=True)
        
        # Key Metrics Cards
        st.markdown("**Key Insights:**")
        
        cols = st.columns(len(selected_companies_summary))
        
        for idx, company in enumerate(selected_companies_summary):
            df_company = df_summary[df_summary['company'] == company]
            if len(df_company) > 0:
                first_price = df_company.sort_values('Date').iloc[0]['Price']
                last_price = df_company.sort_values('Date').iloc[-1]['Price']
                growth_pct = (last_price - first_price) / first_price * 100 if first_price != 0 else 0
                
                with cols[idx]:
                    color = "🟢" if growth_pct >= 0 else "🔴"
                    st.metric(
                        label=company,
                        value=f"₱{last_price:.2f}",
                        delta=f"{growth_pct:.2f}%"
                    )
        
        # Detailed Data Table
        st.markdown("---")
        st.subheader(" Stock Data Table")
        st.markdown("*Weekly Unprocessed Data of all 5 Companies*")
        
        # Prepare detailed data for display
        df_detailed = df_summary[['Date', 'company', 'Price', 'Open', 'High', 'Low', 'Volume', 'Change_pct']].copy()
        df_detailed = df_detailed.sort_values('Date', ascending=False).reset_index(drop=True)
        
        # Format numeric columns for display
        df_detailed_display = df_detailed.copy()
        df_detailed_display['Price'] = df_detailed_display['Price'].apply(lambda x: f"₱{x:.2f}" if pd.notna(x) else "N/A")
        df_detailed_display['Open'] = df_detailed_display['Open'].apply(lambda x: f"₱{x:.2f}" if pd.notna(x) else "N/A")
        df_detailed_display['High'] = df_detailed_display['High'].apply(lambda x: f"₱{x:.2f}" if pd.notna(x) else "N/A")
        df_detailed_display['Low'] = df_detailed_display['Low'].apply(lambda x: f"₱{x:.2f}" if pd.notna(x) else "N/A")
        df_detailed_display['Volume'] = df_detailed_display['Volume'].apply(lambda x: f"{x:,.0f}" if pd.notna(x) else "N/A")
        df_detailed_display['Change_pct'] = df_detailed_display['Change_pct'].apply(lambda x: f"{x:.2f}%" if pd.notna(x) else "N/A")
        df_detailed_display['Date'] = df_detailed_display['Date'].dt.strftime('%Y-%m-%d')
        
        st.dataframe(
            df_detailed_display[['Date', 'company', 'Price', 'Open', 'High', 'Low', 'Volume', 'Change_pct']],
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("📌 Select at least one company to view summary statistics")

except FileNotFoundError:
    st.error("❌ Data file not found at `data/merged_cleaned_stocks.csv`")
    st.info("Please ensure the merged_cleaned_stocks.csv file is in the data folder")
