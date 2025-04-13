# Sample data: dictionary of authors and number of books they've written
authors = {
    "Agatha Christie": 85,
    "J.K. Rowling": 15,
    "George Orwell": 9,
    "Stephen King": 63,
    "Jane Austen": 6,
    "Mark Twain": 28,
    "Haruki Murakami": 23,
    "Toni Morrison": 11,
    "Neil Gaiman": 24,
    "Ernest Hemingway": 7
}

# Sample data: genre and their average sales
genre_sales = {
    "Action": 5166000000,
    "Adventure": 1500000000,
    "Role-Playing": 3200000000,
    "Puzzle": 80000000,
    "Racing": 1200000000,
    "Simulation": 600000000,
    "Strategy": 950000000
}

# Create an empty list
authors_below_twenty_five = []

# Loop through the authors dictionary
for key, value in authors.items():
    
    # Check for values less than 25
    if value < 25:
        
        # Append the author's name to the list
        authors_below_twenty_five.append(key)

# Print the result
print(authors_below_twenty_five)


# Loop through each genre and its average sale value
for genre, average_sale in genre_sales.items():
    
    # Filter for the maximum sales value
    if average_sale == 5166000000:
        print("Most popular genre:", genre)
        print("Average sales:", average_sale)
    
    # Filter for the minimum sales value
    elif average_sale == 80000000:
        print("Least popular genre:", genre)
        print("Average sales:", average_sale)

# Loop through the dictionary
for genre, sale in genre_sales.items():
  
  # Check if genre is Horror or Mystery
  if genre == "Horror" or genre == "Mystery":
    print(genre, sale)
  
  # Check if genre is Thriller and sale is at least 3 million
  elif genre == "Thriller" and sale >= 3000000:
    print(genre, sale)

