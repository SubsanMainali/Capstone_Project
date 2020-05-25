# I will give you a prime number  as long as you wish.


def get_prime(last_number):
    """
    This function returns a prime number next to a given prime number.
    :param last_number: int
    :return: prime number next to last_number
    """
    prime_not_found = True
    while prime_not_found:
        last_number += 1
        factor_count = 0

        # Counting the factors of a number
        for fact_check in range(1, last_number+1):
            if last_number % fact_check == 0:
                factor_count += 1

        # Number is prime if it has only two factors
        if factor_count == 2:
            prime_not_found = False

    return last_number


print("First prime number is 2")
last_prime = 2
wantPrime = True
while wantPrime:

    ask = str(input("Do you want next prime number?(Y/N)"))
    if ask.upper() == 'Y':
        new_prime = get_prime(last_prime)
        last_prime = new_prime
        print(f'Next Prime number is {new_prime}')
    else:
        wantPrime = False
