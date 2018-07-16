"""
2520 は 1 から 10 の数字の全ての整数で割り切れる数字であり, そのような数字の中では最小の値である.

では, 1 から 20 までの整数全てで割り切れる数字の中で最小の正の数はいくらになるか.
"""
from functools import reduce

def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0

list = [x for x in range(1, 21)]
print(reduce(lcm, list, 1))
