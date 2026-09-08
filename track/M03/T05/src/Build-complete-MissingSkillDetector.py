class StudentProfile:
    def __init__(self,skills):
        self.skills = skills

class JobDescription:
    def __init__(self,skills):
        self.skills = skills

class SkillAnalyzer:
    def __init__(self,student,job):
        self.student = student
        self.job = job

    def analyzer(self):
        pass

class MissingSkillDetector(SkillAnalyzer):
    def analyze(self):
        student_skills = []
        for skill in self.student.skills:
            if skill.strip() != "":
                student_skills.append(skill.strip().lower())

        required_skills = []
        for skill in self.job.skills:
            if skill.strip() != "":
                required_skills.append(skill.strip().lower())

        missing_skills = []

        for skill in required_skills:
            if skill not in student_skills:
                missing_skills.append(skill)

        return missing_skills
        
student_skills = input().split(", ")
required_skills = input().split(", ")

student = StudentProfile(student_skills)
job = JobDescription(required_skills)
detector = MissingSkillDetector(student,job)

print(detector.analyze())