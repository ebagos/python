"""
2の平方根は無限に続く連分数で表すことができる.
√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

最初の4回の繰り返しを展開すると以下が得られる.

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

次の3つの項は99/70, 239/169, 577/408である. 第8項は1393/985である. これは分子の桁数が分母の桁数を超える最初の例である.

最初の1000項を考えたとき, 分子の桁数が分母の桁数を超える項はいくつあるか?
"""

"""
分母は1つ前の項の分母+分子、分子は1つ前の項の分母*2+分子
"""
def main():
    bunshi = 3
    bunbo = 2
    koeta = 0
    """
    999回調べればいい
    """
    for i in range(1, 1000):
        nbunbo = bunshi + bunbo
        nbunshi = bunbo * 2 + bunshi
        if len(str(nbunbo)) < len(str(nbunshi)): koeta += 1
        bunbo = nbunbo
        bunshi = nbunshi
    print(koeta)

main()
