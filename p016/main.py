"""
2^15 = 32768 であり, 各位の数字の和は 3 + 2 + 7 + 6 + 8 = 26 となる.

同様にして, 2^1000 の各位の数字の和を求めよ.
"""

def wa(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

def wa2(n):
    return sum(list(int(x) for x in str(n)))

print(wa(2**15))
print(wa(2**1000))

print(wa2(2**15))
print(wa2(2**1000))
