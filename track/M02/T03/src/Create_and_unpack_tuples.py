name = input()
course = input()
score = int(input())

# Create the tuple
student_record = (name,course,score)

# Unpack the tuple
name1, course1, score1 = student_record

# Display the unpacked values
print(f"Name: {name1}")
print(f"Course: {course1}")
print(f"Score: {score1}")
