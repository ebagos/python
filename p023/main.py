"""
完全数とは, その数の真の約数の和がそれ自身と一致する数のことである. たとえば, 28の真の約数の和は, 1 + 2 + 4 + 7 + 14 = 28 であるので, 28は完全数である.

真の約数の和がその数よりも少ないものを不足数といい, 真の約数の和がその数よりも大きいものを過剰数と呼ぶ.

12は, 1 + 2 + 3 + 4 + 6 = 16 となるので, 最小の過剰数である. よって2つの過剰数の和で書ける最少の数は24である. 数学的な解析により, 28123より大きい任意の整数は2つの過剰数の和で書けることが知られている. 2つの過剰数の和で表せない最大の数がこの上限よりも小さいことは分かっているのだが, この上限を減らすことが出来ていない.

2つの過剰数の和で書き表せない正の整数の総和を求めよ.
"""
def make_true_divisor_list(num):
    if num < 1:
        return []
    elif num == 1:
        return [1]
    else:
        divisor_list = []
        divisor_list.append(1)
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                divisor_list.append(i)
        #divisor_list.append(num)

        return divisor_list

def make_divisor_list(num):
    result = make_true_divisor_list(num)
    result.append(num)
    return result

def d(num):
    return sum(make_true_divisor_list(num))

def main():
    MAX = 28123
    med = []
    for i in  range(1, MAX+1):
        if i < d(i):
            med.append(i)
    med2 = [x+y for x in med for y in med]
    result = 0
    for i in range(1, MAX+1):
        if not (i in med2):
            result += 1
    print(result)

main()
