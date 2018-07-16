"""
フィボナッチ数列の項は前の2つの項の和である. 最初の2項を 1, 2 とすれば, 最初の10項は以下の通りである.
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

数列の項の値が400万以下の, 偶数値の項の総和を求めよ.
"""
from tail import tail_recursive

@tail_recursive
def fiboi(n, a1, a2):
    if n < 1:
        return a1
    return fiboi(n-1, a1 + a2, a1)

def fibo(n):
    return fiboi(n, 1, 0)
"""
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n < 1:
        return 0
    else:
        return fibo(n - 1) + fibo(n - 2)
"""

def p002():
    sum = 0
    for n in range(1, 100):
        rc = fibo(n)
        if rc > 4000000:
            return sum
        if rc % 2 == 0:
            print(rc)
            sum = sum + rc

def main():
    return sum(filter(lambda x: x < 4000000 and x % 2 == 0, ([fibo(n) for n in range(1, 100)])))

print(p002())
print(main())

print(fibo(1000))