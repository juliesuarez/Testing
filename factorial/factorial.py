import math
 
print("The factorial of 23 is : ", end="")
print(math.factorial(23))


def calculate_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)
