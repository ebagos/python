"""
125874を2倍すると251748となる. これは元の数125874と順番は違うが同じ数を含む.

2x, 3x, 4x, 5x, 6x が x と同じ数を含むような最小の正整数 x を求めよ.
"""
def check(n, m):
    return sorted(str(n)) == sorted(str(m))

def main():
    n = 1
    while not(check(n, n * 2) and check(n, n * 3) and check(n, n * 4) and check(n, n * 5) and check(n, n * 6)):
        n += 1
    print(n)

main()
