import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [30, 25, 35, None, 28],
    'City': ['Toronto', 'Calgary', 'Montreal', '', 'Toronto']
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Filter: Age > 30
print("\nPeople with Age > 30:")
print(df[df['Age'] > 30])

# Sort: by City name
print("\nSorted by City:")
print(df.sort_values(by='City'))

# Clean: Replace blank City with 'Unknown'
df['City'] = df['City'].replace('', 'Unknown')

# Clean: Fill missing Age with average age
df['Age'] = df['Age'].fillna(df['Age'].mean())

print("\nCleaned DataFrame:")
print(df)

# Analyze: Average Age
print("\nAverage Age:", df['Age'].mean())

# Analyze: Count of people per City
print("\nPeople per City:")
print(df['City'].value_counts())
