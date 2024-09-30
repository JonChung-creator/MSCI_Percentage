# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 16:23:12 2024

@author: jonat
"""

import pandas as pd

# Load the CSV file
input_csv_path = 'C:/Users/jonat/Downloads/ESG Ratings Timeseries Expanded 2017.xlsx'  # Replace with your actual input file path

# Read the data from the CSV file with a specified encoding and handle bad lines
try:
    df = pd.read_csv(input_csv_path, encoding='ISO-8859-1', on_bad_lines='skip')  # Skip bad lines
except Exception as e:
    print(f"An error occurred: {e}")
    df = None  # Set df to None if an error occurs

# Continue only if df was created successfully
if df is not None:
    # Replace empty strings with NaN
    df.replace('', pd.NA, inplace=True)

    # Calculate filled percentage for each column
    filled_percentage = (df.notnull().sum() / len(df)) * 100

    # Prepare the output DataFrame
    output_df = pd.DataFrame({
        'Variable': filled_percentage.index,
        'Filled Percentage': filled_percentage.values
    })

    # Save the output to a new CSV file
    output_csv_path = 'filled_percentage_output.csv'
    output_df.to_csv(output_csv_path, index=False)

    print(f"Output saved to {output_csv_path}")
else:
    print("Data frame not created due to an error in reading the input file.")
