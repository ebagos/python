"""
驚くべきことに, 各桁を4乗した数の和が元の数と一致する数は3つしかない.

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

ただし, 1=1^4は含まないものとする. この数たちの和は 1634 + 8208 + 9474 = 19316 である.

各桁を5乗した数の和が元の数と一致するような数の総和を求めよ.
"""

"""
各桁をn乗した値がもとの値を超えないところを探す必要がある
"""
"""
    fill: 数値nで満たされたc桁の数値を作成する
    cが0のときは0を返すのでエラー処理が必要かもだが、つじつまはあって処理できる
"""
from functools import reduce

def fill(n, c):
    return int(reduce(lambda x, y: x + y, [str(n) for z in range(c)], "0"))
"""
    sum = 0
    for i in range(c+1):

        sum = sum * 10 + n
    return sum
"""
"""
    limit: x乗した数値が元の数値のx乗を超える分岐点を得る
    無限ループで構成すると超えなかったときに戻らないので注意
    境界は9並びの数値で判断するため超えないことはないはずだが・・・
"""
def limit(x):
    MAX = 100
    tmp = 0
    for i in range(MAX):
        tmp = i * 9 ** x
        if fill(9, i) > tmp:
            break
    return tmp

def main():
    POWER = 5
    seed = [n ** POWER for n in range(10)]
    ans = 0
    for s in range(2, limit(POWER)):
        val = sum(map(lambda y: seed[int(y)], str(s)))
        if val == s:
            print("the condition meets with %d" % s)
            ans += val
    print("answer = %d" % ans)

main()

