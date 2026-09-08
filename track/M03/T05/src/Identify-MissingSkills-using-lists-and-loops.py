def find_missing_skills(student_skills, required_skills):
    missing_skills = []

    student_lower = [skill.strip().lower() for skill in student_skills]

    for skill in required_skills:
        if skill not in student_skills:
            original_skill = skill.strip()

            if original_skill.lower() not in student_lower:
                missing_skills.append(original_skill)

    return missing_skills


n = int(input())
student_skills = input().split(",") if n > 0 else []

m = int(input())
required_skills = input().split(",") if m > 0 else []

result = find_missing_skills(student_skills, required_skills)

if result:
    print(",".join(result))
else:
    print("No Missing Skills")