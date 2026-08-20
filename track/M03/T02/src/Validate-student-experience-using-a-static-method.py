class StudentProfile:
    def __init__(self,name,experience):
        self.name = name
        self.experience = experience

    # Create the is_valid_experience() static method
    @staticmethod
    def is_valid_experience(experience):
        if experience >= 0 and experience <= 40:
            return True
        return False

name = input().strip()
experience = int(input())

# Validate the experience using the class name
# Create and print the profile only when experience is valid
if StudentProfile.is_valid_experience(experience):
    student = StudentProfile(name, experience)

    print("PROFILE CREATED")
    print(f"Name: {student.name}")
    print(f"Experience: {student.experience} years")
else:
    print("Invalid Experience")