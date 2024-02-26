import streamlit as st
import pandas as pd

# Sample data
data = {
    'Category': ['A', 'B'],
    'Value_1': [10, 40],
    'Value_2': [20, 50],
    'Value_3': [30, None]  # Add None or NaN for missing values
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set 'Category' column as index
df.set_index('Category', inplace=True)

# Transpose the DataFrame
df_transposed = df.T

# Display the transposed DataFrame
st.table(df_transposed)