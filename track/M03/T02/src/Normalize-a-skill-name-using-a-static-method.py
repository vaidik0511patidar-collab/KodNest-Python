class StudentProfile:
    # Create the normalize_skill() static method
    @staticmethod
    def normalize_skill(skill_name):
        clean = skill_name.strip().lower().split()
        normalize = '_'.join(clean)

        return normalize

skill_name = input()

# Print the normalized skill
print("Normalized Skill:",StudentProfile.normalize_skill(skill_name))