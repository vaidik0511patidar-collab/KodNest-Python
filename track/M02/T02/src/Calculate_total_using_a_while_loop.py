# Read the value of n
n = int(input())

# Initialize the counter and total
counter = 1
total = 0

# Calculate the total using while loop
while counter <= n:
    total += counter
    counter += 1

# Display the total
print("Total: ",total)