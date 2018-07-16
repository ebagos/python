from itertools import groupby

def crle(dat):
    rc = []
    for k, g in groupby(dat):
        rc.append((k, len(list(g))))
    return rc

def crld(dat):
    rc = []
    for (rf, cnt) in dat:
        rc += [rf] * cnt
    return rc

def brle(dat):
    if type(dat) == str or type(dat[0]) == str:
        dat = list(map(int, map(ord, dat)))
    tmp = []
    for c in dat:
        for b in reversed(range(8)):
            tmp.append((c & (1<<b))>>b)
    return crle(tmp)

def brld(dat):
    rc = []
    tmp = crld(dat)
    for i in range(0, len(tmp), 8):
        x = 0
        for s in reversed(range(8)):
            if i + 7 - s > len(tmp) - 1: break
            x += tmp[i + 7 - s] << s
        rc.append(x)
    return rc
