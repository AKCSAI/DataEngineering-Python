# Create a multi-line string named review_one to store the first user review
review_one = """I really enjoy the courses,
and they are easy to fit into my busy schedule. 
I wish I had started using your platform sooner.
I'll be recommending you to my friends!!"""

# Create a multi-line string named review_two to store the second user review
review_two = """One year ago, I was unsure of how to make progress in my career. 
Now, I work as a Prompt Engineer, and I can't thank you enough! 
Keep up the great work."""

# Print the first review to the screen
print(review_one)

# Print the second review to the screen
print(review_two)


# Define a string variable holding the title of a course
most_popular_course = "Intro to Embeddings with the OpenAI API"

# Replace the word "Intro" with "Introduction" in the course title
# Update the first word
most_popular_course = most_popular_course.replace("Intro", "Introduction")

# Swap spaces for underscores
most_popular_course = most_popular_course.replace(" ", "_")

# Change to lowercase
most_popular_course = most_popular_course.lower()

# Print the updated course title to the screen
print(most_popular_course)
