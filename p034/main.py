"""
145は面白い数である. 1! + 4! + 5! = 1 + 24 + 120 = 145となる.

各桁の数の階乗の和が自分自身と一致するような数の和を求めよ.

注: 1! = 1 と 2! = 2 は総和に含めてはならない.
"""

"""
この方法はlimit()で示す検索範囲が大きすぎるため処理時間がかかる
"""
from functools import reduce
from math import factorial

def fill(n, c):
    return int(reduce(lambda x, y: x + y, [str(n) for z in range(c)], "0"))

def limit():
    MAX = 100
    tmp = 0
    for i in range(MAX):
        tmp = i * factorial(9)
        if fill(9, i) > tmp:
            break
    return tmp

def fnc(n):
    return sum(list(factorial(int(i)) for i in str(n)))

def main():
    print(sum(filter(lambda x: fnc(x) == x, range(3, limit()))))

main()
