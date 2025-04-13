tickets_sold = 0
max_capacity = 10

# Create a while loop
while tickets_sold < max_capacity:
  
  # Add one to tickets_sold in each iteration
  tickets_sold += 1



# This program simulates a countdown to a product release date,
# printing different promotional messages depending on the day.

# Number of tickets sold (you'll need to define this variable before running)
tickets_sold = 1500  # <-- Example value, change as needed

# Print how many tickets have been sold so far
print("Sold out:", tickets_sold, "tickets sold!")

# Define the official release date and today's starting date
release_date = 26
current_date = 22

# Loop through each day until and including the release date
while current_date <= release_date:

    # If today is before the 25th, promote early access
    if current_date <= 24:
        print("Purchase before the 25th for early access")

    # If today is the 25th, notify that the release is coming soon
    elif current_date == 25:
        print("Coming soon")

    # If today is the 26th or later, announce that it's available
    else:
        print("Available now!")

    # Move to the next day
    current_date += 1
