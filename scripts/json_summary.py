import json
from utils import get_data_path

json_path = get_data_path("electronicsData.json")

#Open the JSON
with open(json_path, 'r') as file:
    items=json.load(file)

price=[item['price'] for item in items]

total_count= len(price)
total_revenue = sum(price)
max_price = max(price)
min_price = min(price)

#PRINT SUMMARY STATS

print("---- Summary Stats ----")
print(f"Total Items: {total_count}")
print(f"Total Revenue: {total_revenue}")
print(f"Highest Price: {max_price}")
print(f"Lowest Price: {min_price}")
print("--------------------------")