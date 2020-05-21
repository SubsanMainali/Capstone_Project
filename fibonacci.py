# Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to
# the Nth number.

n = 0
flag = 1
while flag:
    try:
        n = abs(int(input("Enter a number")))
        flag = 0
    except ValueError:
        print("Expected a counting number")
        continue


# calculating fibonacci sequence up to nth term
def fibonacci(nth_term, no_of_terms=True):
    a = 1
    b = 1
    if no_of_terms is True:
        for nterm in range(nth_term):
            yield a
            a, b = b, a+b
    else:
        # Calculating Fibonacci sequence term less than n
        while a <= nth_term:
            yield a
            a, b = b, a+b


print(f"Fibonacci sequence up to {n} term :")
for term in fibonacci(n):
    print(str(term)+" ", end=" ")
print()

# Fibonacci sequence term less than n
for term in fibonacci(n, False):
    print(str(term)+" ", end=" ")
print()
