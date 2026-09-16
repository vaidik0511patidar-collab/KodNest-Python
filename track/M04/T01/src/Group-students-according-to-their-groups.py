def group_students(students):
    student_by_course = {}

    for name, course in students:
        if course not in student_by_course:
            student_by_course[course] = []
        student_by_course[course].append(name)

    return student_by_course

n = int(input())

students =  []

for i in range(n):
    name, course  = input().split()
    students.append((name,course))

student_by_course = group_students(students)

for course, name in student_by_course.items():
    print(course + ": " + " ".join(name))