class TrainingBatch:
    # Create the shared batch name
    batch_name = "Python Batch 1"

    def __init__(self, student_name):
        # Store the student name in an instance variable
        self.student_name = student_name

student1_name = input().strip()
student2_name = input().strip()
special_batch = input().strip()
new_shared_batch = input().strip()

# Create two TrainingBatch objects
t1 = TrainingBatch(student1_name)
t2 = TrainingBatch(student2_name)

# Create an object-specific batch value for student1
t1.batch_name = special_batch

# Update the shared class variable
TrainingBatch.batch_name = new_shared_batch

# Print the class and object batch values
print(f"Class Batch: {TrainingBatch.batch_name}")
print(f"{student1_name} Batch: {t1.batch_name}")
print(f"{student2_name} Batch: {t2.batch_name}")