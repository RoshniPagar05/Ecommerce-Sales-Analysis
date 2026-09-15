import pandas as pd
import mysql.connector
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

file_path = os.path.join(
    BASE_DIR,
    "data",
    "ecommerce_sales_cleaned.csv"
)

df = pd.read_csv(file_path)

print("CSV loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))

# Read cleaned CSV
#df = pd.read_csv("../data/ecommerce_sales_cleaned.csv")

# Convert date
df["order_date"] = pd.to_datetime(df["order_date"])

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ecommerce_db"
)

cursor = connection.cursor()

# SQL INSERT statement
sql = """
INSERT INTO sales (
    order_id,
    order_date,
    customer_id,
    customer_name,
    city,
    state,
    category,
    product,
    quantity,
    unit_price,
    payment_method,
    order_status
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s)
"""

# Insert records
for _, row in df.iterrows():

    values = (
        row["order_id"],
        row["order_date"].date(),
        row["customer_id"],
        row["customer_name"],
        row["city"],
        row["state"],
        row["category"],
        row["product"],
        int(row["quantity"]),
        float(row["unit_price"]),
        row["payment_method"],
        row["order_status"]
    )

    cursor.execute(sql, values)

# Save changes
connection.commit()

print("Data successfully inserted into MySQL!")
print("Number of records:", len(df))

cursor.close()
connection.close()