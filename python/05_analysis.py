import pandas as pd
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ecommerce_db"
)
query = """
SELECT
    category,
    SUM(quantity * unit_price) AS revenue
FROM sales
WHERE order_status = 'Completed'
GROUP BY category
ORDER BY revenue DESC
"""

df = pd.read_sql(query, connection)

print(df)

connection.close()


import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.bar(df["category"],df["revenue"])
plt.title("Revenue by category")
plt.xlabel("Category")
plt.ylabel("Revenue")

plt.xticks(rotation=30)
plt.tight_layout()
plt.show()