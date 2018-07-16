"""
以下の三角形の頂点から下まで移動するとき, その数値の和の最大値は23になる.
3
7 4
2 4 6
8 5 9 3

この例では 3 + 7 + 4 + 9 = 23.

以下の三角形を頂点から下まで移動するとき, その最大の和を求めよ.
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

tristr = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""[1:-1]

tri = []
tristrs = [x.split(" ") for x in tristr.split("\n")]
for y in tristrs:
    tri.append([int(x) for x in y])
tri_len = len(tri)
result = tri[0][0]
x = 0
for y in range(1, tri_len):
    if tri[y][x] < tri[y][x+1]:
        x = x + 1
    result += tri[y][x]
    print(y, x, tri[y][x])
print(result)

print(75+95+47+87+82+75+73+28+83+47+43+73+91+67+98)

for y in range(tri_len - 1, 0, -1):
    for x in range(len(tri[y]) - 1):
        if tri[y][x] > tri[y][x+1]:
            tri[y-1][x] += tri[y][x]
        else:
            tri[y-1][x] += tri[y][x+1]
    print(tri[y-1])

print(tri[0][0])