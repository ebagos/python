from rled import crle, crld, brle, brld

data1 = 'AABCCCXXCAADEFFFG'
print("%s => " %data1, end='')
print(brle(data1))
print(brld(brle(data1)))

data2 = [2, 4, 6, 2, 2, 2, 3, 7, 7, 7, 7, 7]
print(data2, end = '')
print(" => ", end='')
print(brle(data2))
print(brld(brle(data2)))

"""
11100111 111 => 0xe7 0xe0
"""
data3 = [(1, 3), (0, 2), (1, 6)]
print(brld(data3))
