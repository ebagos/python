"""
ピタゴラス数(ピタゴラスの定理を満たす自然数)とは a < b < c で以下の式を満たす数の組である.
a2 + b2 = c2

例えば, 32 + 42 = 9 + 16 = 25 = 52 である.

a + b + c = 1000 となるピタゴラスの三つ組が一つだけ存在する.
これらの積 abc を計算しなさい.
"""
from functools import reduce

rc = []
for b in range(500):
    for a in range(1, b):
        c = 1000 - a - b
        if c < b:
            b, c = c, b
        if c * c - b * b - a * a == 0:
            rc = [a, b, c]
            break

print(rc)
print(reduce(lambda x, y: x * y, rc))
            