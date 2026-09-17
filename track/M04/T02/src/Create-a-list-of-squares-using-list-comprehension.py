def create_squares(numbers):
    # Write your list comprehension here

    return [number**2 for number in numbers]


n = int(input())
numbers = map(int,input().split())

squares = create_squares(numbers)

print(*squares)