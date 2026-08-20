class JobDescription:
    platform_name = "KodNest Jobs"

    def __init__(
        self,
        role,
        company,
        minimum_experience
    ):
        # Store the job information
        self.role = role
        self.company = company
        self.minimum_experience = minimum_experience

    # Create the is_valid_experience() static method
    @staticmethod
    def is_valid_experience(experience):
        if experience >= 0 and experience <= 20:
            return True
        return False

    # Create the from_text() class method
    @classmethod
    def from_text(cls, data):
        role, company, experience = data.split("|")

        role = role.strip().title()
        company = company.strip()

        if cls.is_valid_experience(int(experience)):
            return cls(role, company, int(experience))
        else:
            return None


data = input()

# Create the job using from_text()
job = JobDescription.from_text(data)

# Print the job or the invalid message
if job is not None:
    print(f"Platform: {JobDescription.platform_name}")
    print(f"Role: {job.role}")
    print(f"Company: {job.company}")
    print(f"Minimum Experience: {job.minimum_experience} years")
else:
    print("Invalid Experience")