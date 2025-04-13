# Sample data for inflation rates
inflation_august = 3.2
inflation_september = 2.9

# Check if September inflation is less than August inflation
if inflation_september < inflation_august:
  print("Inflation decreased")

# Check if September inflation is more than August inflation
elif inflation_september > inflation_august:
  print("Inflation increased")

# Confirm that they are equal
else: 
  print("Inflation remained stable")


# Sample data
num_beds = 3
min_num_beds = 2

sq_foot = 900
min_sq_foot = 850

rent = 1400
max_rent = 1500

# Check the number of beds
if num_beds < min_num_beds:
    print("Insufficient bedrooms")

# Check square feet
elif sq_foot <= min_sq_foot: 
    print("Too small")

# Check the rent
elif rent > max_rent: 
    print("Too expensive")

# If all conditions met
else: 
    print("This looks promising!")
