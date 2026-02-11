import csv
from utils import get_data_path

csv_path = get_data_path("electronicsData.csv")

#open the csv

with open(csv_path,'r') as file:
    reader= csv.DictReader(file)
    items = list(reader)

#CSV values are read as strings, so lets convert it to float

price = [float(item['price']) for item in items]

total_count = len(price)
total_revenue = sum(price)
max_price = max(price)
min_price = min(price)

#Print the Stats
print("----- Summary Stats -----")
print(f"Total Items: {total_count}")
print(f"Total Revenue: {total_revenue}")
print(f"Highest Price: {max_price}")
print(f"Lowest Price: {min_price}")
print("----------------------------")

