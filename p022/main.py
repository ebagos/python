"""
5000個以上の名前が書かれている46Kのテキストファイル filenames.txt を用いる. まずアルファベット順にソートせよ.

のち, 各名前についてアルファベットに値を割り振り, リスト中の出現順の数と掛け合わせることで, 名前のスコアを計算する.

たとえば, リストがアルファベット順にソートされているとすると, COLINはリストの938番目にある. またCOLINは 3 + 15 + 12 + 9 + 14 = 53 という値を持つ. よってCOLINは 938 × 53 = 49714 というスコアを持つ.

ファイル中の全名前のスコアの合計を求めよ.
"""
from functools import reduce

dict = {'A':1}
def make_dict(dict):
    n = 2
    for x in list('BCDEFGHIJKLMNOPQRSTUVWXYZ'):
        sub = {x:n}
        dict.update(sub)
        n += 1

def name_point(name):
    return reduce(lambda x, y: x + y, map(lambda x:dict[x], name))

f = open('/home/hides/Documents/projects/python/names.txt', mode = 'r')
try:
    text = f.read()
    text = text.strip()
finally:
    f.close()

text = text.replace("\"", "")
names = text.split(",")
names.sort()
make_dict(dict)
n = 1
sum = 0
for name in names:
    sum += name_point(name) * n
    n += 1
print(sum)