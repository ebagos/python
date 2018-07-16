"""
d(n) を n の真の約数の和と定義する. (真の約数とは n 以外の約数のことである. )
もし, d(a) = b かつ d(b) = a (a ≠ b のとき) を満たすとき, a と b は友愛数(親和数)であるという.

例えば, 220 の約数は 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110 なので d(220) = 284 である.
また, 284 の約数は 1, 2, 4, 71, 142 なので d(284) = 220 である.

それでは10000未満の友愛数の和を求めよ.
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
    result = []
    for num in range(1, 10000):
        if num == d(d(num)) and num != d(num):
            result.append(num)
    print(result)
    print(sum(result))

main()
