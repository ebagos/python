"""
Googol (10100)は非常に大きな数である: 1の後に0が100個続く. 100100は想像を絶する. 1の後に0が200回続く. その大きさにも関わらず, 両者とも数字和 ( 桁の和 ) は1である.

a, b < 100 について自然数 ab を考える. 数字和の最大値を答えよ.
"""
def main():
    mx = 0
    for a in range(1, 100):
        for b in range(1, 100):
            n = a ** b
            s = sum(list(int(x) for x in str(n)))
            if mx < s:
                mx = s
    print(mx)

main()
