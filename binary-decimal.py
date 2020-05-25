# Convert a decimal number to binary
# Convert a binary number to decimal


def verify_binary_input():
    """
    Makes sure that the given binary number is in appropriate format.

    :return: Binary number and position of decimal if any.
    """
    number_is_not_binary = True
    b_number = ' '
    decimal_check = 0
    while number_is_not_binary:
        b_number = str(input("Enter a binary number "))
        decimal_count = 0
        for index in range(len(b_number)):
            # Counting the decimal point to make sure that given number is valid
            if b_number[index] == '.':
                decimal_count += 1
                decimal_check = index

            # Checking if given digits are binary
            if b_number[index] == '1' or b_number[index] == '0' or b_number[index] == '.':
                number_is_not_binary = False
            else:
                number_is_not_binary = True

        # Making sure the decimal point is correctly given if any
        if decimal_count > 1:
            number_is_not_binary = True

        if number_is_not_binary is True:
            print("Can't work with given number")

    return b_number, decimal_check


def binary_decimal():
    """
    Converts a binary number to decimal number
    :return:
    """
    given_binary, decimal_position = verify_binary_input()
    integer_part = str(int(float(given_binary)))
    integer_part = integer_part[::-1]

    # Converting digits before decimal
    sum1 = 0
    for i in range(len(integer_part)):
        sum1 += (int(integer_part[i])) * (2 ** i)

    # Converting digits after decimal
    sum2 = 0
    if decimal_position != 0: # decimal_position means given number has no decimal point
        decimal_part = given_binary[decimal_position + 1:]
        for i in range(1, len(decimal_part) + 1):
            sum2 += (int(decimal_part[i - 1])) * (2 ** (-i))
    sum1 += sum2

    # Showing result
    print(f"Decimal number = {sum1}")


def decimal_binary():
    """
    Converts a decimal number into its binary equivalent
    :return:
    """
    flag = True
    # Making sure that the given input is valid
    num = 0
    while flag:
        try:
            num = float(input("Enter a decimal number "))
            flag = False
        except ValueError:
            print("Expected a number")

    # Taking integer part only
    n_digits_after_decimal = len(str(num)) - len(str(int(num))) - 1  # count the number of digits after decimal
    integer_part = int(num)
    binary = ' '
    while integer_part != 0:
        reminder = integer_part % 2
        binary += str(reminder)
        integer_part = int(integer_part/2)

    if n_digits_after_decimal != 0:
        after_decimal = round((num-(int(num))), n_digits_after_decimal)
        binary_after_decimal = ''
        for n_digit in range(n_digits_after_decimal):
            after_decimal *= 2
            binary_after_decimal += str(int(after_decimal))
            after_decimal = round((after_decimal-int(after_decimal)), n_digits_after_decimal)

        # Concatenating both strings
        binary += '.' + binary_after_decimal

    # Showing result
    print(f"Binary equivalent = {binary}")


print("\t\tConverter Menu")
print("_______________________________________")
print("1. Binary to decimal")
print("2. Decimal to binary")
print("3. Exit")

choice = str(input("Pick any one of the options "))
if choice.upper() == '1':
    binary_decimal()
elif choice.upper() == '2':
    decimal_binary()
else:
    print("Program terminated!")

