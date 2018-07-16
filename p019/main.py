"""
次の情報が与えられている.

    1900年1月1日は月曜日である.
    9月, 4月, 6月, 11月は30日まであり, 2月を除く他の月は31日まである.
    2月は28日まであるが, うるう年のときは29日である.
    うるう年は西暦が4で割り切れる年に起こる. しかし, 西暦が400で割り切れず100で割り切れる年はうるう年でない.

20世紀（1901年1月1日から2000年12月31日）中に月の初めが日曜日になるのは何回あるか?
"""
def isUruu(year):
    result = False
    if year % 4 == 0:
        result = True
        if year % 400 != 0 and year % 100 == 0:
            result = False
    return result

def isSun(day):
    if day % 7 == 6:
        return True
    else:
        return False

def problem_19():
    result = 0
    sum_of_days = 0
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sum_of_days = sum(days)
    if not isUruu(1900):
        sum_of_days += 1
    if isSun(sum_of_days):
        result += 1
    for year in range(1901, 2001):
        for month in range(12):
            sum_of_days += days[month]
            if month == 1 and isUruu(year):
                sum_of_days += 1
            if isSun(sum_of_days):
                result += 1
    return result

print(problem_19())

def getdays(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif year % 400 == 0:
        return 29
    elif year % 100 == 0:
        return 28
    elif year % 4 == 0:
        return 29
    else:
        return 28

