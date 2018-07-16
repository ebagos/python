"""
n × (n - 1) × ... × 3 × 2 × 1 を n! と表す.

例えば, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800 となる.
この数の各桁の合計は 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27 である.

では, 100! の各位の数字の和を求めよ.
"""
from math import factorial
from functools import reduce

def wa(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

print(wa(factorial(10)))
print(wa(factorial(100)))

def wa2(n):
    return sum([int(x) for x in str(n)])

print(wa2(factorial(100)))

