# Re-generating the eCommerce dataset after session reset

import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)
num_records = 100000  # Big data simulation

# Generate random order dates
dates = pd.date_range(start="2023-01-01", periods=365, freq='D')
order_dates = np.random.choice(dates, num_records)

# Generate random data
data = {
    "Order ID": np.arange(1, num_records + 1),
    "Order Date": order_dates,
    "Customer ID": np.random.randint(1000, 9999, num_records),
    "Product Category": np.random.choice(["Electronics", "Clothing", "Home & Kitchen", "Sports", "Beauty"], num_records),
    "Product Name": np.random.choice(["Laptop", "Smartphone", "Shoes", "Watch", "Headphones", "Backpack", "Blender"], num_records),
    "Quantity": np.random.randint(1, 5, num_records),
    "Unit Price": np.random.uniform(10, 500, num_records).round(2),
    "Discount": np.random.uniform(0, 0.3, num_records).round(2),
    "Region": np.random.choice(["North America", "Europe", "Asia", "Australia"], num_records),
    "City": np.random.choice(["New York", "London", "Tokyo", "Sydney"], num_records),
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate Total Price (Revenue) after Discount
df["Total Price"] = (df["Quantity"] * df["Unit Price"] * (1 - df["Discount"])).round(2)

# Simulate profit margin
df["Profit"] = (df["Total Price"] * np.random.uniform(0.1, 0.3, num_records)).round(2)

# Save dataset
file_path = "ecommerce_data.csv"
df.to_csv(file_path, index=False)

file_path
