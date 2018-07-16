"""
以下の4言語、4つの挨拶を対話的に表示するプログラムを作成せよ

| 　　 |   日本語   |    英語      | フランス語 |    ドイツ語     |
|:----:|:----------:|:------------:|:----------:|:---------------:|
| 朝　 | おはよう　 | Good moring  |   Bonjour  |  Guten Morgen   |
| 昼　 | こんにちは |    Hello     |   Bonjour  |    Guten Tag    |
| 夜　 | こんばんは | Good evening |   Bonsoir  |   Guten Abend   |
| 別れ | さようなら |   Good-by    |  Au revoir | Auf Wiedersehen |

プログラムは、
1. 最初の入力で言語選択
2. 次の選択でシチュエーション選択
3. 最初に戻る、または終了

- ユーザインタフェースはご自由に！
- 拡張性を考慮すること
"""
JA = ["日本語", "おはよう", "こんにちは", "こんばんは", "さようなら"]
EN = ["English", "Good moring", "Hello", "Good evening", "Good-by"]
FR = ["Français", "Bonjour", "Bonjour", "Bonsoir", "Au revoir"]
GR = ["Deutsch", "Guten Morgen", "Guten Tag", "Guten Abend", "Auf Wiedersehen"]

MESSAGES = [JA, EN, FR, GR]
LANGUAGE = [JA[0], EN[0], FR[0], GR[0]]

def getid(title, disp):
    while True:
        print("\nselect %s" %title)
        for i in range(len(disp)):
            print("%s = %d " %(disp[i], (i+1)), end="")
        print("end = 9 : ", end="")
        try:
            n = int(input())
        except Exception as e:
            print("%r" %e)
            continue
        if n > 0 and n < len(disp) + 1:
            return n
        if n == 9:
            return n

def main():
    while True:
        language_id = getid("Language", LANGUAGE)
        if language_id == 9:
            break
        message_id = getid("Message", MESSAGES[language_id - 1][1:])
        if message_id == 9:
            break
        print(MESSAGES[language_id - 1][message_id])

main()
