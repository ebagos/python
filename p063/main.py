"""
5桁の数 16807 = 75は自然数を5乗した数である. 同様に9桁の数 134217728 = 89も自然数を9乗した数である.

自然数を n 乗して得られる n 桁の正整数は何個あるか?
"""

"""
n乗すべき自然数の最大値は9なのだと仮定して、
9のn乗がn桁を超えない最大値を調べてから解答を求める
"""
def getLimit():
    beki = 1
    while len(str(9 ** beki)) >= beki:
        beki += 1
    return beki

def main():
    nlist = []
    for i in range(1, 10):
        for beki in range(1, getLimit()):
            tgt = i ** beki
            if len(str(tgt)) == beki:
                nlist.append(tgt)
            beki += 1
    print(nlist)
    print(len(nlist))
 
main()
