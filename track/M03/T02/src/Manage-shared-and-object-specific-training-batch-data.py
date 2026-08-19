class TrainingBatch:
    # Create the share class variables
    platform_name = "KodNest"
    batch_name = "Python Batch 1"

    def __init__(self, student_name, score):
        # Store the object specific values
        self.student_name = student_name
        self.score = score

student1_name = input().strip()
student1_score = int(input())

student2_name = input().strip()
student2_score = int(input())

# Create two TrainingBatch objects
t1 = TrainingBatch(student1_name, student1_score)
t2 = TrainingBatch(student2_name, student2_score)

# Print the shared batch information
print("Platform:",TrainingBatch.platform_name)
print("Batch:",TrainingBatch.batch_name)

# Print the information of both the students
print(f"Student 1: {t1.student_name}, Score: {t1.score}")
print(f"Student 2: {t2.student_name}, Score: {t2.score}")