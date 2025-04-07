import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Load dataset
file_path = "ecommerce_data.csv"  # Update this if needed
df = pd.read_csv(file_path)

# Keep only necessary columns
df = df[['Order ID', 'Product Name']]

# Pivot data to a transaction format
basket = df.pivot_table(index='Order ID', columns='Product Name', aggfunc=lambda x: 1, fill_value=0)

# Apply Apriori Algorithm
frequent_itemsets = apriori(basket, min_support=0.01, use_colnames=True)

# Generate Association Rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)

# Display results
print("Frequent Itemsets:")
print(frequent_itemsets)

print("\nAssociation Rules:")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
