import pandas as pd

# -----------------------------
# 1. EXTRACT
# -----------------------------
# Load CSV files into DataFrames
products = pd.read_csv('products.csv')
customers = pd.read_csv('customers.csv')
orders = pd.read_csv('orders.csv')

# -----------------------------
# 2. TRANSFORM
# -----------------------------

# 2.1 JOIN DATASETS
# Join orders with customers on CustomerID
orders_customers = pd.merge(orders, customers, on='CustomerID', how='left')

# Join the result with products on ProductID
full_data = pd.merge(orders_customers, products, on='ProductID', how='left')

# 2.2 ADD NEW COLUMNS
# TotalAmount = Quantity * Price
full_data['TotalAmount'] = full_data['Quantity'] * full_data['Price']

# OrderMonth = extract month from OrderDate
full_data['OrderDate'] = pd.to_datetime(full_data['OrderDate'])
full_data['OrderMonth'] = full_data['OrderDate'].dt.month

# 2.3 FILTER DATA
# Remove orders with Quantity < 2
filtered_data = full_data[full_data['Quantity'] >= 2]

# Keep only customers from India or UAE
filtered_data = filtered_data[filtered_data['Country'].isin(['India', 'UAE'])]

# 2.4 GROUP & AGGREGATE
# Total revenue per Category
category_summary = filtered_data.groupby('Category', as_index=False)['TotalAmount'].sum()

# Total revenue per Customer Segment
segment_summary = filtered_data.groupby('Segment', as_index=False)['TotalAmount'].sum()

# 2.5 SORTING & RANKING
# Sort customers by total revenue (highest to lowest)
customer_revenue = (
    filtered_data.groupby(['CustomerID', 'Name', 'Country', 'Segment'], as_index=False)['TotalAmount']
    .sum()
    .sort_values(by='TotalAmount', ascending=False)
)

# -----------------------------
# 3. LOAD
# -----------------------------

# Save processed enriched data
processed_orders = filtered_data[['OrderID', 'CustomerID', 'Name', 'Country', 'Segment',
                                  'ProductName', 'Category', 'Quantity', 'Price',
                                  'TotalAmount', 'OrderDate', 'OrderMonth']]

processed_orders.to_csv('processed_orders.csv', index=False)
category_summary.to_csv('category_summary.csv', index=False)
segment_summary.to_csv('segment_summary.csv', index=False)
customer_revenue.to_csv('customer_ranking.csv', index=False)

print("✅ ETL Pipeline completed successfully!")
print("Files generated:")
print(" - processed_orders.csv")
print(" - category_summary.csv")
print(" - segment_summary.csv")
print(" - customer_ranking.csv")