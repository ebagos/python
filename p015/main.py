"""
2×2 のマス目の左上からスタートした場合, 引き返しなしで右下にいくルートは 6 つある.
p_15.gif

では, 20×20 のマス目ではいくつのルートがあるか.
"""
"""
40C20=40P20/20!
"""
n = 20
m = 40

# mPn
p = 1
for i in range(m, n, -1):
  p *= i

# n!
bo = 1
for i in range(1, n+1):
  bo *= i

result = p // bo

print(result)

"""
from scipy.special import comb

print(int(comb(40, 20)))
"""
