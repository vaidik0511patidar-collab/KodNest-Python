class StudentProfile:
    # Create class level object-counter
    profile_count = 0

    def __init__(self,name):
        # Store the name
        # Increase the object counter
        self.name = name
        StudentProfile.profile_count += 1

n = int(input())
students = []

# Read n names and create n StudentProfile objects
for student in range(n):
    student_name = input().strip()
    student = StudentProfile(student_name)
    students.append(student)

# Display the total number of StudentProfile objects created
print("Profiles Created:",StudentProfile.profile_count)