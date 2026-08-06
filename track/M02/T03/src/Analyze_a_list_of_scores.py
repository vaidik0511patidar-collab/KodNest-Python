n = int(input())
scores = []

# Read and store all scores
for i in range(n):
    score = int(input())
    scores.append(score)

search_score = int(input())

# Display the highest, lowest and total scores
print(f"Highest Score: {max(scores)}")
print(f"Lowest Score: {min(scores)}")
print(f"Total Score: {sum(scores)}")

# Display whether search_score is present
if search_score in scores:
    print("Search Result: Found")
else:
    print("Search Result: Not Found")