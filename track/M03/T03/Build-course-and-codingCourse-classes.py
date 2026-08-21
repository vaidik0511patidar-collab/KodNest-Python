class Course:
    # Add the constructor and display_course()
    def __init__(self,course_name):
        self.course_name = course_name

    def display_course(self):
        print("Course:",self.course_name)

class CodingCourse(Course):
    pass

course_name = input().strip()

# Create a CodingCourse object and call display_course() method
student1 = CodingCourse(course_name)
student1.display_course()