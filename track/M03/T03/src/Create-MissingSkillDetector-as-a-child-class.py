class SkillAnalyzer:
    def __init__(self, student_skills, required_skills):
        self.student_skills = set(student_skills)
        self.required_skills = set(required_skills)

    def get_matched_skills(self):
        return self.student_skills & self.required_skills

class MissingSkillDetector(SkillAnalyzer):
    # Add get_missing_skills()
    def get_missing_skills(self):
        return set(self.required_skills) - set(self.get_matched_skills())

student_skills = input().split()
required_skills = input().split()

# Create the detector and display the missing skills in alphabetical order
detector = MissingSkillDetector(student_skills, required_skills)
missing = sorted(detector.get_missing_skills())

if missing:
    print(f"Missing Skills: {', '.join(missing)}")
else:
    print("Missing Skills: None")