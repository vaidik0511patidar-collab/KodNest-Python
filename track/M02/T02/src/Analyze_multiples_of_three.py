limit = int(input())
target = int(input())

count = 0
total = 0
found = "No"

# Examine every number from 1 to the limit
for i in range(1,limit+1):
    if i % 3 == 0:
        count += 1
        total += i
    if i % 3 == 0 and i == target:
        found = "Yes"

# Display the count, total and search result
print("Count: ",count)
print("Sum: ",total)
print("Target Found: ",found)