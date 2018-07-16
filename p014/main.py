"""
正の整数に以下の式で繰り返し生成する数列を定義する.

    n → n/2 (n が偶数)

    n → 3n + 1 (n が奇数)

13からはじめるとこの数列は以下のようになる.
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

13から1まで10個の項になる. この数列はどのような数字からはじめても最終的には 1 になると考えられているが, まだそのことは証明されていない(コラッツ問題)

さて, 100万未満の数字の中でどの数字からはじめれば最長の数列を生成するか.

注意: 数列の途中で100万以上になってもよい
"""
"""
def collatz(n, iter):
    if n == 1:
        return iter
    if n % 2 == 0:
        return collatz(n/2, iter + 1)
    else:
        return collatz(3 * n + 1, iter + 1)

ans = 0
for i in range(2, 999999):
    rc = collatz(i, 1)
    if rc > ans: ans = rc
print(ans)
"""
def next(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

def add(dict, n1):
    n2 = next(n1)
    if not n2 in dict:
        dict = add(dict, n2)
    dict[n1] = dict[n2] + 1
    return dict

def main():
    dict = {1:1}
    (max_i, max) = (1, 1)
    for i in range(2, 10 ** 6):
        if not i in dict:
            dict = add(dict, i)
            if dict[i] > max:
                (max_i, max) = (i, dict[i])
    print((max_i, max))

main()