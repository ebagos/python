"""
各文字はそれぞれ一意のコードに割り当てられている. よく使われる標準としてASCII (American Standard Code for Information Interchange) がある. ASCIIでは, 大文字A = 65, アスタリスク (*) = 42, 小文字k = 107というふうに割り当てられている.

モダンな暗号化の方法として, テキストファイルの各バイトをASCIIに変換し, 秘密鍵から計算された値とXORを取るという手法がある. XOR関数の良い点は, 暗号化に用いたのと同じ暗号化鍵でXORを取ると平文を復号できる点である. 65 XOR 42 = 107であり, 107 XOR 42 = 65である.

破られない暗号化のためには, 鍵は平文と同じ長さのランダムなバイト列でなければならない. ユーザーは暗号文と暗号化鍵を別々の場所に保存する必要がある. また, もし一方が失われると, 暗号文を復号することは不可能になる.

悲しいかな, この手法はほとんどのユーザーにとって非現実的である. そこで, 鍵の変わりにパスワードを用いる手法が用いられる. パスワードが平文より短ければ (よくあることだが), パスワードは鍵として繰り返し用いられる. この手法では, 安全性を保つために十分長いパスワードを用いる必要があるが, 記憶するためにはある程度短くないといけない.

この問題での課題は簡単になっている. 暗号化鍵は3文字の小文字である. cipher1.txtは暗号化されたASCIIのコードを含んでいる. また, 平文はよく用いられる英単語を含んでいる. この暗号文を復号し, 平文のASCIIでの値の和を求めよ.
"""

"""
英文だからスペースが一番多いものが正解というかなりあれな根拠から解く
"""

import csv
from functools import reduce

def to_int_list(data):
    rc = []
    for c in data:
        rc.append(int(c))
    return rc

def read_data():
    data = []
    with open('/home/hides/Documents/projects/python/cipher1.txt', newline='') as f:
        dataReader = csv.reader(f)
        for row in dataReader:
            data += row
    return to_int_list(data)

def main():
    alpha = range(ord('a'), ord('z') + 1)
    data = read_data()
    mspc = 0
    for a0 in alpha:
        for a1 in alpha:
            for a2 in alpha:
                spc = 0
                seed = [a0, a1, a2]
                text = [chr(x ^ seed[i % 3]) for i, x in enumerate(data)]
                spc = text.count(' ')
                if spc > mspc:
                    mspc = spc
                    mseed = seed
                    mtext = text
    print("seed:", reduce(lambda a, b: a+b, list(map(lambda x: chr(x), mseed))))
    print("".join(mtext))

main()
