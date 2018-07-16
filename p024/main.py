"""
順列とはモノの順番付きの並びのことである. たとえば, 3124は数 1, 2, 3, 4 の一つの順列である. すべての順列を数の大小でまたは辞書式に並べたものを辞書順と呼ぶ. 0と1と2の順列を辞書順に並べると
012 021 102 120 201 210
になる.

0,1,2,3,4,5,6,7,8,9からなる順列を辞書式に並べたときの100万番目はいくつか?
"""
from math import factorial

def main():
    target = 10 ** 6
    target -= 1
    answer = ''
    ls = [x for x in range(10)]
    for i in range(9, -1, -1):
        n = ls.pop(target // factorial(i))
        target %= factorial(i)
        answer += str(n)
    print('answer = %s' % answer)

main()

def fmain(target, answer, seed, iter):
    if iter == -1:
        return answer
    n = seed.pop(target // factorial(iter))
    return fmain(target % factorial(iter), answer + str(n), seed, iter - 1)

print('answer = %s' % fmain(10**6 - 1, '', [x for x in range(10)], 9))
