# Read the course details
course_name = input()
current_week = input()
course_status = input()

# Create the original tuple
course_details = (course_name,current_week,course_status)

# Read the updated week
updated_week = input()

# Create and assign the new tuple
new_tuple = (course_name,updated_week,course_status)
course_details = new_tuple

# Display the updated tuple
print(course_details)