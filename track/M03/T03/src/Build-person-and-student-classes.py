class Person:
    # Create the display_name() here
    def display_name(self,name):
        print("Student Name:",name)

class Student(Person):
    pass

name = input().strip()

# Create a Student object and call display_name() method
s1 = Student()
s1.display_name(name)