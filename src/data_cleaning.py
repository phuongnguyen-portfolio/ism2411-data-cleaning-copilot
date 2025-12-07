"""This script cleans a messy sales dataset to a cleaned version"""
import pandas as pd
# Load raw data
def load_data(file_path):
    """Load data from a CSV file into a pandas DataFrame."""
    return pd.read_csv(file_path)
# Standardize column names, because consistent naming is crucial for analysis
def standardize_column_names(df):
    """Standardize column names to lowercase with underscores."""
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df
# Strip leading/trailing whitespace from product names and categories
def clean_string_columns(df):
    """Clean string columns by stripping whitespace."""
    string_cols = df.select_dtypes(include=['object']).columns
    numeric_cols = ['qty', 'price']
    for col in string_cols:
        df[col] = df[col].str.strip().str.lower().str.replace('"', '').str.replace("'", "")
    return df
# Handle missing values, because missing sales amounts should be treated as the mean
def handle_missing_values(df):
    """Handle missing values by filling or dropping."""
    # Convert qty to numeric, coercing errors to NaN
    df['qty'] = pd.to_numeric(df['qty'], errors='coerce')
    df['qty'] = df['qty'].fillna(df['qty'].mean())
    df['qty'] = df['qty'].round().astype(int)
    df = df[df['date_sold'].notna()]        
    df = df[df['date_sold'].str.strip() != '']
    df = df.dropna(subset=['prodname', 'date_sold'])
    return df
# Remove rows with invalid data, becase negative quantities and prices are data entry errors
def remove_invalid_data(df):
    """Remove rows with invalid data."""
    # Convert price and qty to numeric, coercing errors to NaN
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['qty'] = pd.to_numeric(df['qty'], errors='coerce')
    df = df[df['qty'] >= 0]
    df = df[df['price'] >= 0]
    return df
if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"
    df_raw = load_data(raw_path)
    df_clean = standardize_column_names(df_raw)
    df_clean = clean_string_columns(df_clean)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_data(df_clean)
    df_clean.to_csv(cleaned_path, index=False)
    print("Cleaning complete. First few rows:")
    print(df_clean.head())
