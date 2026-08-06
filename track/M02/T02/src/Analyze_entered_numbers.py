# Read how many numbers will be entered
n = int(input())

# Initialize the counters and total
positive = 0
negative = 0
zero = 0
total = 0

# Read and analyze each number
for i in range(1,n+1):
    number = int(input())

    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zero += 1

    total += number

# Display the final analysis
print(f"Positive Count: {positive}")
print(f"Negative Count: {negative}")
print(f"Zero Count: {zero}")
print(f"Total: {total}")