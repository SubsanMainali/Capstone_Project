# Calculate factorial of a given number
# Making sure the value is a positive integer
# This program cannot handle very large numbers; maximum value is 998


# recursive function to calculate factorial
def factorial(number):
    if number == 0:
        return 1
    elif number == 1:
        return number
    else:
        return number*factorial(number-1)


num = 0
flag = True
while flag:
    try:
        num = int(input("Enter a counting number"))
        flag = False
        num = abs(num)
    except ValueError:
        print("Expected a counting number")

print(f'Factorial of {num} is {factorial(num)}')

