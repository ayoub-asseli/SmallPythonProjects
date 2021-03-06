"""
A Fibonacci Word is a specific sequence of binary digits (or symbols from any two-letter alphabet). The Fibonacci Word is formed by repeated concatenation in the same way that the Fibonacci numbers are formed by repeated addition.

Create a function that takes a number n as an argument and returns the first n elements of the Fibonacci Word sequence.

If n < 2, the function must return "invalid".

Examples
fibo_word(1) ➞ "invalid"

fibo_word(3) ➞ "b, a, ab"

fibo_word(7) ➞ "b, a, ab, aba, abaab, abaababa, abaababaabaab"
"""


def fibo_word(n):
    if n < 2:
        return 'invalid'
    s0, s1 = 'b', 'a'
    res = 'b, a'
    for i in range(2, n):
        s2 = s1 + s0
        res += ', ' + s2
        s0, s1 = s1, s2
    return res
