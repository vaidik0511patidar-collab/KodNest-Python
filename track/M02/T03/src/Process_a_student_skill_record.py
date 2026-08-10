skills = []

# Read and store five skills
for _ in range(5):
    skills.append(input())

# Convert the list into a tuple
skill_record = tuple(skills)

# Create the required slices
first_three = skill_record[0:3]
last_two = skill_record[-2:]
alternate = skill_record[::2]
reverse = skill_record[::-1]

# Display all required results
print(f"Skill Record: {skill_record}")
print(f"First Three: {first_three}")
print(f"Last Two: {last_two}")
print(f"Alternate Skills: {alternate}")
print(f"Reversed Skills: {reverse}")