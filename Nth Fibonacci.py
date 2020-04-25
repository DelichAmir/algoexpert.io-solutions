# The Fibonacci sequence is dened as follows: the rst number of the
# sequence is 0 , the second number is 1 , and the nth number is the
# sum of the (n - 1)th and (n - 2)th numbers. Write a function that takes in
# an integer n and returns the nth Fibonacci number.
# Important note: the Fibonacci sequence is often dened with its rst two
# numbers as F0 = 0 and F1 = 1 . For the purpose of this question,
# the rst Fibonacci number is F0 ; therefore, getNthFib(1) is equal to
# F0 , getNthFib(2) is equal to F1 , etc..

# Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def getNthFib(n: int) -> int:
    # First solution
    # if n == 1:
    #     return 0
    # elif n == 2:
    #     return 1
    # else:
    #     return getNthFib(n-1) + getNthFib(n-2)

    # Second Solution
    mem = {1: 0, 2: 1}
    for i in range(3, n+1):
        mem[i] = mem[i-1] + mem[i-2]

    print(f'The number {n} in Fibonacci is:', mem[n])
    return mem[n]


# Test cases:
assert getNthFib(2) == 1
assert getNthFib(6) == 5
assert getNthFib(10) == 34