class Employee:
    # Add the constructor
    def __init__(self,name):
        self.name = name

class Developer(Employee):
    # Add the constructor and display_profile()
    def __init__(self,name,language):
        super().__init__(name)
        self.language = language

    def display_profile(self):
        print("Employee:",self.name)
        print("Language:",self.language)

name = input().strip()
language = input().strip()

# Create a Developer object and call display_profile() method
user = Developer(name,language)
user.display_profile()