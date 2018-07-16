"""
10未満の自然数のうち, 3 もしくは 5 の倍数になっているものは 3, 5, 6, 9 の4つがあり, これらの合計は 23 になる.

同じようにして, 1000 未満の 3 か 5 の倍数になっている数字の合計を求めよ.
"""

print(sum(list(filter(lambda x: x % 3 == 0 or x % 5 == 0, list(range(1, 1000))))))

print(sum([i for i in range(1, 1000) if i % 3 * i % 5 == 0]))

print(sum(set(list(range(3, 1000, 3)) + list(range(5, 1000, 5)))))
