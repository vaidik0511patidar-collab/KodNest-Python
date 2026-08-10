def calculate(first_number, second_number, operator):
    # Write your code here
    if operator == '+':
        return first_number + second_number
    elif operator == '-':
        return first_number - second_number
    elif operator == '*':
        return first_number * second_number
    else:
        return first_number / second_number


first_number = int(input())
second_number = int(input())
operator = input().strip()

result = calculate(first_number, second_number, operator)
print(result)