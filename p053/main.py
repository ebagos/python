"""
12345から3つ選ぶ選び方は10通りである.
123, 124, 125, 134, 135, 145, 234, 235, 245, 345.

組み合わせでは, 以下の記法を用いてこのことを表す: 5C3 = 10.

一般に, r ≤ n について nCr = n!/(r!(n-r)!) である. ここで, n! = n×(n−1)×...×3×2×1, 0! = 1 と階乗を定義する.

n = 23 になるまで, これらの値が100万を超えることはない: 23C10 = 1144066.

1 ≤ n ≤ 100 について, 100万を超える nCr は何通りあるか?
"""

dicto = {1: 1}

def factorial(n):
    def sub(n, s):
        if n == 0:
            return s
        else:
            return sub(n-1, s * n)
    return sub(n, 1)

def p053_1(a):
    rc = 0
    for n in range(1, a + 1):
        for r in range(1, n):
            x = int(factorial(n))//int((factorial(r) * factorial(n - r)))
            if x > 1000000:
                rc += 1
    return rc

def fact(n):
    if not n in dicto:
        dicto[n] = n * fact(n - 1)
    return dicto[n]

def p053_2(a):
    rc = 0
    for n in range(1, a + 1):
        for r in range(1, n):
            x = fact(n)/(fact(r) * fact(n - r))
            if (x > 1000000):
                rc += 1
    return rc

print(p053_1(100))
print(p053_2(100))
