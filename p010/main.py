"""
10以下の素数の和は 2 + 3 + 5 + 7 = 17 である.

200万以下の全ての素数の和を求めよ.
"""
from functools import reduce

def primes(max):
    result = [2]
    i = 3
    while i < max:
        for p in result:
            if i % p == 0:
                break
        else:
            result += [i]
        i += 2
    return result

def main():
    max = 2000001
    rlist = primes(max)
    print(reduce(lambda x, y: x + y, rlist))

main()
