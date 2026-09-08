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

class MatchScoreCalculator(SkillAnalyzer):
    def analyze(self):
        student_skills = []
        for skill in self.student.skills:
            if skill.strip() != "":
                student_skills.append(skill.strip().lower())

        required_skills = []
        for skill in self.job.skills:
            if skill.strip() != "":
                required_skills.append(skill.strip().lower())

        if len(required_skills) == 0:
            return 0

        match_score = 0

        for skill in required_skills:
            if skill in student_skills:
                match_score += 1

        return match_score / len(required_skills) * 100
        
student_skills = input().split(", ")
required_skills = input().split(", ")

student = StudentProfile(student_skills)
job = JobDescription(required_skills)
calculator = MatchScoreCalculator(student,job)

print(calculator.analyze())