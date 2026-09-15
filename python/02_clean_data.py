import pandas as pd
from pathlib import Path
#find project folder auomatically
project_folder= Path(__file__).resolve().parent.parent

#create path to csv file
csv_file= project_folder / "data" / "ecommerce_sales.csv"

#read csv file
df= pd.read_csv(csv_file)

print("Original Shape:",df.shape)

#---------------------
#1 check missing values
#----------------------

print("\nMissing Values before cleaning:")
print(df.isnull().sum())

#-------------------
#2 check duplicated rows
#---------------------

print("\nDuplicated rows before cleaning:")
print(df.duplicated().sum())

#-----------------------------
# 3 convert order_date to date
#--------------------------------
df["order_date"]=pd.to_datetime(df["order_date"])

#---------------------------
# 4 remove duplicate  rows
# ---------------------------
df=df.drop_duplicates()

#------------------------
# 5 handle missing values
#--------------------------

df["city"]=df["city"].fillna("UnKnown")
df["payment_method"]=df["payment_method"].fillna("UnKnown")

#-------------------------------
# 6 convert numeric columns
#-------------------------------

df["quantity"]=pd.to_numeric(
    df["quantity"],
    errors="coerce"
)
df["unit_price"]=pd.to_numeric(
    df["unit_price"],
    errors="coerce"
)

#----------------------
#7 remove rows with missing quantity or price
#---------------------
df=df.dropna(
    subset=["quantity","unit_price"]

)

#--------------------
#8 calculate total amount
#---------------------

df["total_amount"]=(
    df["quantity"] * df["unit_price"]
    )

#-------------------------
#final information
#--------------------------

print("\nCleaned shape:")
print(df.shape)

print("\nMissing Values after cleaning:")
print(df.isnull().sum())

print("\nFirst 5 cleaned records:")
print(df.head())

#----------------------------
#save final dataset
#--------------------------------

output_file = (
    project_folder
    / "data"
    / "ecommerce_sales_cleaned.csv"
)

df.to_csv(output_file, index=False)

print("\nCleaned dataset saved successfully!")
print("File:", output_file)