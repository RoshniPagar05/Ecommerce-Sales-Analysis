import pandas as pd

from pathlib import Path

# Get the project folder
project_folder = Path(__file__).resolve().parent.parent

# Build the CSV file path
csv_file = project_folder / "data" / "ecommerce_sales.csv"

# Read CSV
df = pd.read_csv(csv_file)

#display 5 records
print("First 5 Record:")
print(df.head())

#display no of rows and columns
print("\nDataset shape:")
print(df.shape)

#display column names
print("\nColumn names:")
print(df.columns.tolist())

#print display information
print("\nDataset information:")
print(df.info())