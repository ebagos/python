"""
素数を小さい方から6つ並べると 2, 3, 5, 7, 11, 13 であり, 6番目の素数は 13 である.

10 001 番目の素数を求めよ.
"""
def primes(n):
    prime_list = [2]
    i = 3
    while len(prime_list) < n:
        for p in prime_list:
            if i % p == 0:
                break
        else:
            prime_list += [i]
        i += 2
    return prime_list

def main():
    n = 10001
    pl = primes(n)
    result = pl[-1]
    print(result)

main()
