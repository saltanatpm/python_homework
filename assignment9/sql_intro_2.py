import sqlite3
import pandas as pd

conn = sqlite3.connect("../db/lesson.db")
query = """
SELECT
    line_items.line_item_id,
    line_items.quantity,
    line_items.product_id,
    products.product_name,
    products.price
FROM line_items
JOIN products
ON line_items.product_id = products.product_id;
"""
df = pd.read_sql_query(query, conn)

# Print first 5 rows
print("FIRST 5 ROWS (RAW DATA):")
print(df.head())

# Create total column
df["total"] = df["quantity"] * df["price"]
print("\nFIRST 5 ROWS (WITH TOTAL):")
print(df.head())

summary = df.groupby("product_id").agg({
    "line_item_id": "count",
    "total": "sum",
    "product_name": "first"
}).reset_index()

summary = summary.sort_values("product_name")

print("\nGROUPED & SORTED SUMMARY:")
print(summary.head())

summary.to_csv("order_summary.csv", index=False)
print("\nSaved file: order_summary.csv")
conn.close()