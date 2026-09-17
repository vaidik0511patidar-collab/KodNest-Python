def select_students(students, cutoff):
    # Write your list comprehension here

    return [student for student in students if student[1] > cutoff]


students = [
    ["Asha", 78],
    ["Neha", 25],
    ["Aman", 70],
    ["Shreya", 85],
    ["Hemant", 90]
]

cutoff = int(input())
selected_students = select_students(students, cutoff)

if not selected_students:
    print("No students selected.")
else:
    for student in selected_students:
        print(student[0])