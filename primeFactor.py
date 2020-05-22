# Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.
import time
import math
num = 0
flag = 1
while flag:
    try:
        num = abs(int(input("Enter a number to find is prime factors ")))
        flag = 0
    except ValueError:
        print("Oops! Expected a counting number.")
        continue


def primeFactors(n):
    # Print the number of two's that divide n
    while n % 2 == 0:
        print(str(2)+" ")
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        u_limit = int(math.sqrt(n))
        # while i divides n , print i ad divide n
        while n % i == 0:
            print(str(i)+" ")
            n = n / i

            # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print(str(int(n)))


t1 = time.time()
primeFactors(num)
t2 = time.time()
print(f"Time taken= {t2-t1}")


