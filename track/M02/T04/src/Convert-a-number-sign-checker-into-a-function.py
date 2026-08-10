def check_sign(number):
    # Write your code here
    if number == 0:
        return "Zero"
    elif number > 0:
        return "Positive"
    else:
        return "Negative"


number = int(input())
result = check_sign(number)
print(result)