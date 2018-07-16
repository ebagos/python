"""
13195 の素因数は 5, 7, 13, 29 である.

600851475143 の素因数のうち最大のものを求めよ.
"""
def prime_decompo(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table

xxx = 600851475143
plist = prime_decompo(xxx)
print(plist[len(plist) - 1])
