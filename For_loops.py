# Create the tickets_sold variable
tickets_sold = 0 

# Create the max_capacity variable
max_capacity = 30

# Loop through a range up to and including max_capacity's value
for i in range(tickets_sold, max_capacity):
  
  # Add one to tickets_sold in each iteration
    tickets_sold += 1
  
print("Sold out:", tickets_sold, "tickets sold!")



# Sample dictionary of courses where key is course name and value is course category
courses = {"LLM Concepts": "AI", 
           "Introduction to Data Pipelines": "Data Engineering", 
           "AI Ethics": "AI",
           "Introduction to dbt": "Data Engineering", 
           "Writing Efficient Python Code": "Programming",
           "Introduction to Docker": "Programming"
           }

# Loop through the dictionary's keys and values
for key, value in courses.items():
    
    # Check if the course is AI
    if value == "AI":
        print(key, "is an AI course")
    
    # Check if the course is Programming
    elif value == "Programming":
        print(key, "is a Programming course")
    
    # Otherwise, treat it as a Data Engineering course
    else:
        print(key, "is a Data Engineering course")

