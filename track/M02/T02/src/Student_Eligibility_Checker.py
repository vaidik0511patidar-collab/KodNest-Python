# Read marks, attendance and project completion status
from string import templatelib
marks = int(input())
attendance = int(input())
project_completion_status = input()

# Check the academic requirements
if marks >= 60 and attendance >= 75:
    # Check the project completion status
    if project_completion_status == "yes":
        print("Eligible for Placements")
    else:
        print("Not Eligible for Placements")
else:
    print("Not Eligible for Placements")