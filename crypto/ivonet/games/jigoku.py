#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# g = [([1, 7, 9, 8, 2, 4, 3, 6, 5], [4, 2, 5, 3, 1, 6, 8, 9, 7], [8, 6, 3, 9, 7, 5, 2, 4, 1], [6, 5, 7, 9, 4, 8, 2, 1, 3], [9, 4, 3, 1, 6, 2, 5, 7, 8], [1, 8, 2, 5, 3, 7, 6, 9, 4], [7, 9, 6, 4, 8, 2, 5, 3, 1], [2, 5, 4, 6, 3, 1, 7, 8, 9], [3, 1, 8, 7, 5, 9, 4, 2, 6]), ([1, 7, 9, 8, 3, 4, 2, 6, 5], [4, 3, 5, 2, 1, 6, 8, 9, 7], [8, 6, 2, 9, 7, 5, 1, 4, 3], [6, 5, 7, 9, 4, 8, 3, 1, 2], [9, 4, 2, 1, 6, 3, 5, 7, 8], [3, 8, 1, 5, 2, 7, 6, 9, 4], [7, 9, 6, 4, 8, 3, 5, 2, 1], [3, 5, 4, 6, 2, 1, 7, 8, 9], [2, 1, 8, 7, 5, 9, 4, 3, 6]), ([1, 7, 9, 8, 3, 4, 2, 6, 5], [4, 3, 5, 2, 1, 6, 8, 9, 7], [8, 6, 2, 9, 7, 5, 3, 4, 1], [6, 5, 7, 9, 4, 8, 3, 1, 2], [9, 4, 2, 1, 6, 3, 5, 7, 8], [1, 8, 3, 5, 2, 7, 6, 9, 4], [7, 9, 6, 4, 8, 3, 5, 2, 1], [3, 5, 4, 6, 2, 1, 7, 8, 9], [2, 1, 8, 7, 5, 9, 4, 3, 6]), ([2, 7, 9, 8, 3, 4, 1, 6, 5], [3, 4, 5, 2, 1, 6, 8, 9, 7], [8, 6, 1, 9, 7, 5, 2, 4, 3], [5, 4, 7, 9, 1, 8, 3, 2, 6], [9, 2, 3, 5, 6, 4, 1, 7, 8], [1, 8, 6, 3, 2, 7, 5, 9, 4], [7, 9, 3, 4, 8, 2, 6, 5, 1], [4, 5, 2, 6, 3, 1, 7, 8, 9], [6, 1, 8, 7, 5, 9, 4, 3, 2]), ([2, 7, 9, 8, 3, 4, 1, 6, 5], [4, 3, 5, 2, 1, 6, 8, 9, 7], [8, 6, 1, 9, 7, 5, 2, 4, 3], [4, 5, 7, 9, 1, 8, 6, 2, 3], [9, 2, 3, 5, 6, 4, 1, 7, 8], [1, 8, 6, 3, 2, 7, 5, 9, 4], [7, 9, 6, 3, 8, 2, 5, 4, 1], [3, 5, 2, 6, 4, 1, 7, 8, 9], [4, 1, 8, 7, 5, 9, 6, 3, 2]), ([2, 7, 9, 8, 3, 4, 1, 6, 5], [4, 3, 5, 2, 1, 6, 8, 9, 7], [8, 6, 1, 9, 7, 5, 2, 4, 3], [5, 4, 7, 9, 1, 8, 6, 2, 3], [9, 2, 3, 5, 6, 4, 1, 7, 8], [1, 8, 6, 3, 2, 7, 5, 9, 4], [7, 9, 6, 3, 8, 2, 4, 5, 1], [3, 5, 2, 6, 4, 1, 7, 8, 9], [4, 1, 8, 7, 5, 9, 6, 3, 2]), ([2, 7, 9, 8, 3, 4, 1, 6, 5], [4, 3, 5, 2, 1, 6, 8, 9, 7], [8, 6, 1, 9, 7, 5, 2, 4, 3], [6, 5, 7, 9, 1, 8, 4, 2, 3], [9, 2, 3, 5, 6, 4, 1, 7, 8], [1, 8, 4, 3, 2, 7, 5, 9, 6], [7, 9, 6, 3, 8, 2, 5, 4, 1], [3, 5, 2, 6, 4, 1, 7, 8, 9], [4, 1, 8, 7, 5, 9, 6, 3, 2]), ([2, 7, 9, 8, 3, 4, 1, 6, 5], [4, 3, 5, 2, 1, 6, 8, 9, 7], [8, 6, 1, 9, 7, 5, 2, 4, 3], [6, 5, 7, 9, 2, 8, 4, 1, 3], [9, 2, 3, 1, 6, 4, 5, 7, 8], [1, 8, 4, 5, 3, 7, 6, 9, 2], [7, 9, 6, 3, 8, 2, 5, 4, 1], [3, 5, 2, 6, 4, 1, 7, 8, 9], [4, 1, 8, 7, 5, 9, 3, 2, 6]), ([3, 7, 9, 8, 2, 4, 1, 6, 5], [4, 2, 5, 3, 1, 6, 8, 9, 7], [8, 6, 1, 9, 7, 5, 2, 4, 3], [6, 5, 7, 9, 4, 8, 2, 1, 3], [9, 4, 3, 1, 6, 2, 5, 7, 8], [1, 8, 2, 5, 3, 7, 6, 9, 4], [7, 9, 6, 4, 8, 2, 5, 3, 1], [2, 5, 4, 6, 3, 1, 7, 8, 9], [3, 1, 8, 7, 5, 9, 4, 2, 6])]


def uniques(g):
    for i in range(9):
        for j in range(9):
            seen = []
            for k in g:
                if k[i][j] not in seen:
                    seen += [k[i][j]]
            print(i, j, seen)


def a(num):
    if num == []:
        yield []
    for i in num:
        numCopy = num[:]
        numCopy.remove(i)
        for b in a(numCopy):
            yield [i] + b


def allSingle(l):
    seen = []
    for i in l:
        if i in seen:
            return False
        seen += [i]
    return True


def checkVer2(p0, p1):
    l1 = p0[::3] + p1[::3]
    l2 = p0[1::3] + p1[1::3]
    l3 = p0[2::3] + p1[2::3]
    if allSingle(l1) and allSingle(l2) and allSingle(l3):
        return True
    return False


def checkVer3(p0, p1, p2):
    l1 = p0[::3] + p1[::3] + p2[::3]
    l2 = p0[1::3] + p1[1::3] + p2[1::3]
    l3 = p0[2::3] + p1[2::3] + p2[2::3]
    if allSingle(l1) and allSingle(l2) and allSingle(l3):
        return True
    return False


def checkHor2(p0, p1):
    l1 = p0[:3] + p1[:3]
    l2 = p0[3:6] + p1[3:6]
    l3 = p0[6:] + p1[6:]
    if allSingle(l1) and allSingle(l2) and allSingle(l3):
        return True
    return False


def checkHor3(p0, p1, p2):
    l1 = p0[:3] + p1[:3] + p2[:3]
    l2 = p0[3:6] + p1[3:6] + p2[3:6]
    l3 = p0[6:] + p1[6:] + p2[6:]
    if allSingle(l1) and allSingle(l2) and allSingle(l3):
        return True
    return False


# def checkHor(p0, p1, p2):
#     done0 = [p0[0], p0[1], p0[2]]
#     for i in range(3):
#         if p1[i] not in done0:
#             done0.append(p0[i])
#         else:
#             return False
#     for i in range(3):
#         if p2[i] not in done0:
#             done0.append(p0[i])
#         else:
#             return False
#     return True
#     done1 = [p0[3], p0[4], p0[5]]
#     for i in range(3,6):
#         if p1[i] not in done1:
#             done1.append(p1[i])
#         else:
#             return False
#     for i in range(3,6):
#         if p2[i] not in done1:
#             done1.append(p1[i])
#         else:
#             return False

#     done2 = [p0[6], p0[7], p0[8]]
#     for i in range(6,9):
#         if p1[i] not in done2:
#             done2.append(p2[i])
#         else:
#             return False
#     for i in range(6,9):
#         if p2[i] not in done2:
#             done2.append(p2[i])
#         else:
#             return False
#     return True


def check0(pos):
    r = []
    for p in pos[:]:
        if not p[8] == 5:
            continue
        if not p[2] > p[1]:
            continue
        if not p[1] > p[4]:
            continue
        if not p[3] > p[4]:
            continue
        if not p[5] > p[4]:
            continue
        if not p[7] > p[8]:
            continue
        if not p[8] > p[5]:
            continue
        r.append(p)
    return r


def check1(pos):
    r = []
    for p in pos[:]:
        if not p[0] in [4, 3]:
            continue
        if not p[5] in [6, 7]:
            continue
        if not p[7] == 9:
            continue
        if not p[0] > p[3]:
            continue
        if not p[3] > p[4]:
            continue
        if not p[5] > p[4]:
            continue
        if not p[2] > p[1]:
            continue
        if not p[5] > p[2]:
            continue
        if not p[7] > p[8]:
            continue
        r.append(p)
    return r


def check2(pos):
    r = []
    for p in pos:
        if not p[1] == 6:
            continue
        if not p[3] == 9:
            continue
        if not p[8] in [1, 3]:
            continue
        if not p[0] > p[1]:
            continue
        if not p[3] > p[0]:
            continue
        if not p[4] > p[7]:
            continue
        if not p[4] > p[5]:
            continue
        if not p[5] > p[2]:
            continue
        if not p[7] > p[8]:
            continue
        r.append(p)
    return r


def check3(pos):
    r = []
    for p in pos:
        if not p[2] > p[1]:
            continue
        if not p[1] > p[4]:
            continue
        if not p[3] > p[6]:
            continue
        if not p[6] > p[7]:
            continue
        if not p[8] > p[7]:
            continue
        if not p[5] > p[4]:
            continue
        if not p[5] > p[2]:
            continue
        r.append(p)
    return r


def check4(pos):
    r = []
    for p in pos:
        if not p[8] == 8:
            continue
        if not p[0] == 9:
            continue
        if not p[4] > p[2]:
            continue
        if not p[4] > p[3]:
            continue
        if not p[4] > p[5]:
            continue
        if not p[7] > p[4]:
            continue
        r.append(p)
    return r


def check5(pos):
    r = []
    for p in pos:
        if not p[7] == 9:
            continue
        if not p[1] > p[0]:
            continue
        if not p[1] > p[2]:
            continue
        if not p[3] > p[4]:
            continue
        if not p[5] > p[2]:
            continue
        if not p[5] > p[8]:
            continue
        if not p[6] > p[3]:
            continue
        if not p[7] > p[6]:
            continue
        if not p[7] > p[4]:
            continue
        r.append(p)
    return r


def check6(pos):
    r = []
    for p in pos:
        if not p[1] == 9:
            continue
        if not p[2] in [3, 6]:
            continue
        if not p[4] == 8:
            continue
        if not p[1] > p[0]:
            continue
        if not p[1] > p[4]:
            continue
        if not p[4] > p[3]:
            continue
        if not p[4] > p[7]:
            continue
        if not p[7] > p[8]:
            continue
        if not p[6] > p[3]:
            continue
        if not p[2] > p[5]:
            continue
        if not p[5] > p[8]:
            continue
        r.append(p)
    return r


def check7(pos):
    r = []
    for p in pos:
        if not p[8] == 9:
            continue
        if not p[1] > p[0]:
            continue
        if not p[3] > p[4]:
            continue
        if not p[4] > p[5]:
            continue
        if not p[8] > p[5]:
            continue
        if not p[8] > p[7]:
            continue
        if not p[7] > p[6]:
            continue
        if not p[6] > p[3]:
            continue
        r.append(p)
    return r


def check8(pos):
    r = []
    for p in pos:
        if not p[5] == 9:
            continue
        if not p[0] > p[1]:
            continue
        if not p[3] > p[0]:
            continue
        if not p[3] > p[4]:
            continue
        if not p[5] > p[4]:
            continue
        if not p[4] > p[7]:
            continue
        if not p[6] > p[7]:
            continue
        r.append(p)
    return r


# Do a test decoding
g = []
if __name__ == '__main__':
    p = []
    q = [None] * 9
    for i in a([1, 2, 3, 4, 5, 6, 7, 8, 9]):
        p.append(i)
    print(len(p))
    q[0] = check0(p[:])
    print('Num pos for 0: ', len(q[0]))
    q[1] = check1(p[:])
    print('Num pos for 1: ', len(q[1]))
    q[2] = check2(p[:])
    print('Num pos for 2: ', len(q[2]))
    q[3] = check3(p[:])
    print('Num pos for 3: ', len(q[3]))
    q[4] = check4(p[:])
    print('Num pos for 4: ', len(q[4]))
    q[5] = check5(p[:])
    print('Num pos for 5: ', len(q[5]))
    q[6] = check6(p[:])
    print('Num pos for 6: ', len(q[6]))
    q[7] = check7(p[:])
    print('Num pos for 7: ', len(q[7]))
    q[8] = check8(p[:])
    print('Num pos for 8: ', len(q[8]))
    f = 0
    # print(q[0][0])
    # print(q[1][0])
    # print(q[2][0])
    for i in q[0]:
        for j in q[1]:
            if not checkHor2(i, j):
                continue
            for k in q[2]:
                if not checkHor3(i, j, k):
                    continue
                for l in q[3]:
                    if not checkVer2(i, l):
                        continue
                    for m in q[4]:
                        if not checkVer2(j, m):
                            continue
                        if not checkHor2(l, m):
                            continue
                        for n in q[5]:
                            if not checkHor3(l, m, n):
                                continue
                            if not checkVer2(k, n):
                                continue
                            for o in q[6]:
                                if not checkVer3(i, l, o):
                                    continue
                                for r in q[7]:
                                    if not checkVer3(j, m, r):
                                        continue
                                    if not checkHor2(o, r):
                                        continue
                                    for s in q[8]:
                                        if not checkVer3(k, n, s):
                                            continue
                                        if not checkHor3(o, r, s):
                                            continue
                                        g.append((i, j, k, l, m, n, o, r, s))
    print(len(g))
