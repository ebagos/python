"""
最初の10個の自然数について, その二乗の和は,
12 + 22 + ... + 102 = 385

最初の10個の自然数について, その和の二乗は,
(1 + 2 + ... + 10)2 = 3025

これらの数の差は 3025 - 385 = 2640 となる.

同様にして, 最初の100個の自然数について二乗の和と和の二乗の差を求めよ.
"""
from functools import reduce

def sumpow(n):
    return ((1+n) * n // 2) ** 2

def powsum(n):
    l = [x**2 for x in range(1, n + 1)]
    return reduce(lambda x, y: x + y, l)

print(sumpow(10))
print(powsum(10))

print(sumpow(100) - powsum(100))