"""
左右どちらから読んでも同じ値になる数を回文数という. 2桁の数の積で表される回文数のうち, 最大のものは 9009 = 91 × 99 である.

では, 3桁の数の積で表される回文数の最大値を求めよ.
"""

def kai(n):
    rc = 0
    while n > 0:
        rc = rc * 10 + (n % 10)
        n = n // 10
    return rc

rc = 0
for a in range(999, 100, -1):
    for b in range(999, a, -1):
        x = a * b
        if (x == kai(x)):
            if (rc < x):
                rc = x

print(rc)

def main():
    rc = 0
    for a in range(999, 100, -1):
        for b in range(999, a, -1):
            x = a * b
            if str(x) == str(x)[::-1]:
                if (rc < x): rc = x
    print(rc)

main()
