def convert_to_fahrenheit(celsius_temperatures):
    # Write your list comprehension here

    return [(celsius_temperature * 9/5) + 32 for celsius_temperature in celsius_temperatures]


n = int(input())
celsius_temperatures = map(int, input().split())

fahrenheit_temperatures = convert_to_fahrenheit(celsius_temperatures)

print(*fahrenheit_temperatures)