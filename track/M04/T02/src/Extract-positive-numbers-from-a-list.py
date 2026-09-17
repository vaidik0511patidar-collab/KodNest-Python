def extract_positive_numbers(numbers):
    # Write your list comprehension here

    return [number for number in numbers if number > 0]


n = int(input())
numbers = map(int, input().split())

positive_numbers = extract_positive_numbers(numbers)

if positive_numbers:
    print(*positive_numbers)
else:
    print("No positive numbers")