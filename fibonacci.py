"""
sequences in python
"""

def fibonacci(x):
    if x <= 0:
        return []
    elif x == 1:
        return [1]
    # elif x == 2:
    #     return [1, 2]

    fib_list = [1, 2]
    while len(fib_list) < x:
        next_fib = fib_list[-1] + fib_list[-2]
        fib_list.append(next_fib)

    return fib_list

print(fibonacci(5))

  #my pair is vanessa Nalugya  