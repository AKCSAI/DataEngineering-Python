# Import pandas as pd
import pandas as pd 

# Sample data: List of dictionaries representing sales records
sales = [
    {"product": "Laptop", "units_sold": 150, "price": 1200},
    {"product": "Smartphone", "units_sold": 300, "price": 800},
    {"product": "Tablet", "units_sold": 200, "price": 400},
    {"product": "Headphones", "units_sold": 500, "price": 150},
    {"product": "Smartwatch", "units_sold": 120, "price": 250}
]

# Convert sales to a pandas DataFrame
sales_df = pd.DataFrame(sales)

# Preview the first five rows
print(sales_df.head())
