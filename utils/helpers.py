"""
Utility functions for the ISEA Finals Dashboard
Shared helper functions used across multiple pages
"""

import streamlit as st
import pandas as pd
from pathlib import Path
from typing import List, Tuple, Optional


# ============================================================================
# DATA LOADING UTILITIES
# ============================================================================

def load_data_from_directory(data_dir: str = "data") -> dict:
    """
    Load all CSV and Excel files from a directory.
    
    Parameters:
    -----------
    data_dir : str
        Path to the directory containing data files
    
    Returns:
    --------
    dict
        Dictionary with filenames as keys and dataframes as values
    """
    data_path = Path(data_dir)
    datasets = {}
    
    if not data_path.exists():
        return datasets
    
    supported_extensions = {'.csv', '.xlsx', '.xls', '.parquet', '.json'}
    
    for file_path in data_path.glob('*'):
        if file_path.suffix.lower() in supported_extensions:
            try:
                if file_path.suffix.lower() == '.csv':
                    datasets[file_path.name] = pd.read_csv(file_path)
                elif file_path.suffix.lower() in ['.xlsx', '.xls']:
                    datasets[file_path.name] = pd.read_excel(file_path)
                elif file_path.suffix.lower() == '.parquet':
                    datasets[file_path.name] = pd.read_parquet(file_path)
                elif file_path.suffix.lower() == '.json':
                    datasets[file_path.name] = pd.read_json(file_path)
            except Exception as e:
                st.warning(f"Could not load {file_path.name}: {str(e)}")
    
    return datasets


@st.cache_data
def cached_load_data(filepath: str) -> pd.DataFrame:
    """
    Load data with caching for better performance.
    
    Parameters:
    -----------
    filepath : str
        Path to the data file
    
    Returns:
    --------
    pd.DataFrame
        Loaded dataframe
    """
    if filepath.endswith('.csv'):
        return pd.read_csv(filepath)
    elif filepath.endswith(('.xlsx', '.xls')):
        return pd.read_excel(filepath)
    elif filepath.endswith('.parquet'):
        return pd.read_parquet(filepath)
    elif filepath.endswith('.json'):
        return pd.read_json(filepath)
    else:
        raise ValueError(f"Unsupported file format: {filepath}")


# ============================================================================
# DATA EXPLORATION UTILITIES
# ============================================================================

def get_data_summary(df: pd.DataFrame) -> dict:
    """
    Generate a summary of dataset statistics.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    
    Returns:
    --------
    dict
        Dictionary containing summary statistics
    """
    return {
        'rows': len(df),
        'columns': len(df.columns),
        'memory_usage': f"{df.memory_usage(deep=True).sum() / 1024**2:.2f} MB",
        'missing_values': df.isnull().sum().sum(),
        'duplicates': df.duplicated().sum(),
        'data_types': df.dtypes.value_counts().to_dict(),
    }


def get_column_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Get detailed statistics for all columns.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    
    Returns:
    --------
    pd.DataFrame
        Statistics for each column
    """
    stats = []
    
    for col in df.columns:
        col_stats = {
            'Column': col,
            'Type': str(df[col].dtype),
            'Non-Null': df[col].notna().sum(),
            'Null': df[col].isna().sum(),
            'Unique': df[col].nunique(),
        }
        
        if pd.api.types.is_numeric_dtype(df[col]):
            col_stats.update({
                'Mean': f"{df[col].mean():.2f}" if not df[col].isna().all() else "—",
                'Std': f"{df[col].std():.2f}" if not df[col].isna().all() else "—",
                'Min': f"{df[col].min():.2f}" if not df[col].isna().all() else "—",
                'Max': f"{df[col].max():.2f}" if not df[col].isna().all() else "—",
            })
        
        stats.append(col_stats)
    
    return pd.DataFrame(stats)


def filter_dataframe(df: pd.DataFrame, 
                     filters: dict) -> pd.DataFrame:
    """
    Apply multiple filters to a dataframe.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    filters : dict
        Filter specifications (column: value pairs)
    
    Returns:
    --------
    pd.DataFrame
        Filtered dataframe
    """
    filtered_df = df.copy()
    
    for column, value in filters.items():
        if value is not None and column in filtered_df.columns:
            if isinstance(value, list):
                filtered_df = filtered_df[filtered_df[column].isin(value)]
            else:
                filtered_df = filtered_df[filtered_df[column] == value]
    
    return filtered_df


# ============================================================================
# VISUALIZATION UTILITIES
# ============================================================================

def get_numeric_columns(df: pd.DataFrame) -> List[str]:
    """
    Get list of numeric columns in a dataframe.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    
    Returns:
    --------
    List[str]
        List of numeric column names
    """
    return df.select_dtypes(include=['number']).columns.tolist()


def get_categorical_columns(df: pd.DataFrame) -> List[str]:
    """
    Get list of categorical columns in a dataframe.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    
    Returns:
    --------
    List[str]
        List of categorical column names
    """
    return df.select_dtypes(include=['object']).columns.tolist()


# ============================================================================
# UI HELPER UTILITIES
# ============================================================================

def display_metric_card(title: str, value: str, 
                       delta: Optional[str] = None,
                       icon: str = "📊") -> None:
    """
    Display a styled metric card.
    
    Parameters:
    -----------
    title : str
        Metric title
    value : str
        Metric value
    delta : str, optional
        Change information
    icon : str
        Icon to display
    """
    st.metric(label=f"{icon} {title}", value=value, delta=delta)


def create_two_column_layout(left_content, right_content) -> None:
    """
    Create a two-column layout with provided content.
    
    Parameters:
    -----------
    left_content : callable
        Function to render left column
    right_content : callable
        Function to render right column
    """
    col1, col2 = st.columns(2)
    
    with col1:
        left_content()
    
    with col2:
        right_content()


# ============================================================================
# EXPORT UTILITIES
# ============================================================================

def export_dataframe_to_csv(df: pd.DataFrame, filename: str) -> bytes:
    """
    Convert dataframe to CSV bytes for download.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    filename : str
        Output filename
    
    Returns:
    --------
    bytes
        CSV data as bytes
    """
    return df.to_csv(index=False).encode('utf-8')


def export_dataframe_to_excel(df: pd.DataFrame, filename: str) -> bytes:
    """
    Convert dataframe to Excel bytes for download.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    filename : str
        Output filename
    
    Returns:
    --------
    bytes
        Excel data as bytes
    """
    import io
    
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
    
    return output.getvalue()
