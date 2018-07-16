"""
各桁の2乗を足し合わせて新たな数を作ることを, 同じ数が現れるまで繰り返す.

例えば

　　44 → 32 → 13 → 10 → 1 → 1
　　85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

のような列である. どちらも1か89で無限ループに陥っている.
驚くことに, どの数から始めても最終的に1か89に到達する.

では, 10,000,000より小さい数で89に到達する数はいくつあるか.
"""
from datetime import datetime

def main():
    count = 0
    MAX = 9 ** 2 * 7 + 1
    memo = [-1 for i in range(MAX)]
    memo[1] = 0
    memo[89] = 1
    for i in range(2, 10000000):
        #print(i)
        n = i
        while True:
            #n = sum([int(x) ** 2 for x in str(n)])
            n = sum([(ord(x) - 48) * (ord(x) - 48) for x in str(n)])
            if memo[n] != -1:
                break
        
        if memo[n] == 1:
            count += 1
            if i < MAX:
                memo[i] = 1
        elif i < MAX:
            memo[i] = 0
    
    print(count)
 
start = datetime.now()
main()
end = datetime.now()
print("elapsed time :", end - start)
