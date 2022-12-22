# A
def a():
    for y in range(7):
        aw = ""
        for x in range(5):
            if y == 0:
                if x == 0:
                    aw = aw + " "
                if x == 1 or x == 2 or x == 3:
                    aw = aw + "*"
                if x == 4:
                    aw = aw + " "
            if y == 1 or y == 2 or y == 4 or y == 5 or y == 6:
                if x == 0:
                    aw = aw + "*"
                if x == 1 or x == 2 or x == 3:
                    aw = aw + " "
                if x == 4:
                    aw = aw + "*"
            if y == 3:
                aw = aw + "*"
        print(aw)

# B


def b():
    for y in range(7):
        aw = ""
        for x in range(5):
            if y == 0 or y == 3 or y == 6:
                if x == 0 or x == 1 or x == 2 or x == 3:
                    aw = aw + "*"
                if x == 4:
                    aw = aw + " "
            if y == 1 or y == 2 or y == 4 or y == 5:
                if x == 0:
                    aw = aw + "*"
                if x == 1 or x == 2 or x == 3:
                    aw = aw + " "
                if x == 4:
                    aw = aw + "*"
    print(aw)

# C


def c():
    for y in range(7):
        aw = ""
        for x in range(5):
            if y == 0 or y == 6:
                if x == 1 or x == 2 or x == 3:
                    aw = aw + "*"
                if x == 0 or x == 4:
                    aw = aw + " "
            if y == 1 or y == 5:
                if x == 0 or x == 4:
                    aw = aw + "*"
                if x == 1 or x == 2 or x == 3:
                    aw = aw + " "
            if y == 2 or y == 3 or y == 4:
                if x == 0:
                    aw = aw + "*"
        print(aw)

# D


def d():
    for y in range(7):
        aw = ""
        for x in range(5):
            if y == 0 or y == 6:
                if x == 0 or x == 1 or x == 2 or x == 3:
                    aw = aw + "*"
                if x == 4:
                    aw = aw + " "
            if y == 1 or y == 2 or y == 3 or y == 4 or y == 5:
                if x == 0:
                    aw = aw + "*"
                if x == 1 or x == 2 or x == 3:
                    aw = aw + " "
                if x == 4:
                    aw = aw + "*"
        print(aw)

# E


def e():
    for y in range(7):
        aw = ""
        for x in range(5):
            if y == 0 or y == 6:
                if x == 0 or x == 1 or x == 2 or x == 3 or x == 4:
                    aw = aw + "*"
                if x == 4:
                    aw = aw + " "
            if y == 1 or y == 2 or y == 4 or y == 5:
                if x == 0:
                    aw = aw + "*"
                if x == 1 or x == 2 or x == 3:
                    aw = aw + " "
            if y == 3:
                if x == 0 or x == 1 or x == 2:
                    aw = aw + "*"
        print(aw)

# F


def f():
    for y in range(7):
        aw = ""
        for x in range(5):
            if y == 0:
                if x == 0 or x == 1 or x == 2 or x == 3 or x == 4:
                    aw = aw + "*"
                if x == 4:
                    aw = aw + " "
            if y == 1 or y == 2 or y == 4 or y == 5 or y == 6:
                if x == 0:
                    aw = aw + "*"
                if x == 1 or x == 2 or x == 3:
                    aw = aw + " "
            if y == 3:
                if x == 0 or x == 1 or x == 2:
                    aw = aw + "*"
    print(aw)

# G


def g():
    for y in range(7):
        aw = ""
        for x in range(5):
            if y == 0 or y == 6:
                if x == 1 or x == 2 or x == 3:
                    aw = aw + "*"
                if x == 0 or x == 4:
                    aw = aw + " "
            if y == 1 or y == 4 or y == 5:
                if x == 0 or x == 4:
                    aw = aw + "*"
                if x == 1 or x == 2 or x == 3:
                    aw = aw + " "
            if y == 2:
                if x == 0:
                    aw = aw + "*"
            if y == 3:
                if x == 0 or x == 3 or x == 4:
                    aw = aw + "*"
                if x == 1 or x == 2:
                    aw = aw + " "
        print(aw)


# H
def h():
    for y in range(7):
        aw = ""
        for x in range(5):
            if y == 0 or y == 1 or y == 2 or y == 4 or y == 5 or y == 6:
                if x == 0 or x == 4:
                    aw = aw + "*"
                if x == 1 or x == 2 or x == 3:
                    aw = aw + " "
            if y == 3:
                aw = aw + "*"
        print(aw)

# I


def i():
    for y in range(7):
        aw = ""
        for x in range(5):
            if y == 0 or y == 6:
                if x == 1 or x == 2 or x == 3:
                    aw = aw + "*"
                if x == 0 or x == 4:
                    aw = aw + " "
            if y == 1 or y == 2 or y == 3 or y == 4 or y == 5:
                if x == 2:
                    aw = aw + "*"
                if x == 0 or x == 1 or x == 3 or x == 4:
                    aw = aw + " "
        print(aw)

# J


def j():
    for y in range(7):
        aw = ""
        for x in range(5):
            if y == 0:
                if x == 1 or x == 2 or x == 3:
                    aw = aw + "*"
                if x == 0 or x == 4:
                    aw = aw + " "
            if y == 1 or y == 2 or y == 3 or y == 4 or y == 5:
                if x == 2:
                    aw = aw + "*"
                if x == 0 or x == 1 or x == 3 or x == 4:
                    aw = aw + " "
            if y == 6:
                if x == 0 or x == 1:
                    aw = aw + "*"
        print(aw)

# K


def k():
    for y in range(7):
        aw = ""
        for x in range(5):
            if y == 0 or y == 6:
                if x == 0 or x == 4:
                    aw = aw + "*"
                if x == 1 or x == 2 or x == 3:
                    aw = aw + " "
            if y == 1 or y == 5:
                if x == 0 or x == 3:
                    aw = aw + "*"
                if x == 1 or x == 2 or x == 4:
                    aw = aw + " "
            if y == 2 or y == 4:
                if x == 0 or x == 2:
                    aw = aw + "*"
                if x == 1 or x == 3 or x == 4:
                    aw = aw + " "
            if y == 3:
                if x == 0 or x == 1:
                    aw = aw + "*"
                if x == 2 or x == 3 or x == 4:
                    aw = aw + " "
        print(aw)

# L


def l():
    for y in range(7):
        aw = ""
        for x in range(5):
            if y == 0 or y == 1 or y == 2 or y == 3 or y == 4 or y == 5:
                if x == 0:
                    aw = aw + "*"
            if y == 6:
                aw = aw + "*"
        print(aw)

# M


def m():
    for y in range(7):
        aw = ""
        for x in range(5):
            if y == 0 or y == 1 or y == 4 or y == 5 or y == 6:
                if x == 0:
                    aw = aw + "*"
                if x == 1 or x == 2 or x == 3:
                    aw = aw + " "
                if x == 4:
                    aw = aw + "*"
            if y == 2:
                if x == 0 or x == 1 or x == 3 or x == 4:
                    aw = aw + "*"
                if x == 2:
                    aw = aw + " "
            if y == 3:
                if x == 1 or x == 3:
                    aw = aw + " "
                if x == 0 or x == 2 or x == 4:
                    aw = aw + "*"
        print(aw)

# N


def n():
    for y in range(7):
        aw = ""
        for x in range(5):
            if y == 0 or y == 1 or y == 5 or y == 6:
                if x == 0:
                    aw = aw + "*"
                if x == 1 or x == 2 or x == 3:
                    aw = aw + " "
                if x == 4:
                    aw = aw + "*"
            if y == 2:
                if x == 0 or x == 1 or x == 4:
                    aw = aw + "*"
                if x == 2 or x == 3:
                    aw = aw + " "
            if y == 4:
                if x == 0 or x == 3 or x == 4:
                    aw = aw + "*"
                if x == 1 or x == 2:
                    aw = aw + " "
            if y == 3:
                if x == 1 or x == 3:
                    aw = aw + " "
                if x == 0 or x == 2 or x == 4:
                    aw = aw + "*"
        print(aw)

# O


def o():
    for y in range(7):
        aw = ""
        for x in range(5):
            if y == 0 or y == 6:
                if x == 0 or x == 4:
                    aw = aw + " "
                if x == 1 or x == 2 or x == 3:
                    aw = aw + "*"
            if y == 1 or y == 2 or y == 3 or y == 4 or y == 5:
                if x == 0 or x == 4:
                    aw = aw + "*"
                if x == 1 or x == 2 or x == 3:
                    aw = aw + " "
        print(aw)

# P


def p():
    for y in range(7):
        aw = ""
        for x in range(5):
            if y == 0 or y == 3:
                if x == 1 or x == 2 or x == 3:
                    aw = aw + "*"
            if y == 0 or y == 1 or y == 2 or y == 3 or y == 4 or y == 5 or y == 6:
                if x == 0:
                    aw = aw + "*"
            if y == 1 or y == 2:
                if x == 4:
                    aw = aw + "*"
            if y == 1 or y == 2:
                if x == 1 or x == 2 or x == 3:
                    aw = aw + " "
        print(aw)

# Q


def q():
    for y in range(7):
        aw = ""
        for x in range(5):
            if y == 0:
                if x == 0 or x == 4:
                    aw = aw + " "
                if x == 1 or x == 2 or x == 3:
                    aw = aw + "*"
            if y == 1 or y == 2 or y == 3 or y == 4:
                if x == 0 or x == 4:
                    aw = aw + "*"
                if x == 1 or x == 2 or x == 3:
                    aw = aw + " "
            if y == 5:
                if x == 1 or x == 2 or x == 4:
                    aw = aw + " "
                if x == 0 or x == 3:
                    aw = aw + "*"
            if y == 6:
                if x == 0 or x == 3:
                    aw = aw + " "
                if x == 1 or x == 2 or x == 4:
                    aw = aw + "*"
        print(aw)

# R


def r():
    for y in range(7):
        aw = ""
        for x in range(5):
            if y == 0 or y == 3:
                if x == 0 or x == 1 or x == 2 or x == 3:
                    aw = aw + "*"
                if x == 4:
                    aw = aw + " "
            if y == 1 or y == 2:
                if x == 0:
                    aw = aw + "*"
                if x == 1 or x == 2 or x == 3:
                    aw = aw + " "
                if x == 4:
                    aw = aw + "*"
            if y == 4:
                if x == 0 or x == 2:
                    aw = aw + "*"
                if x == 1 or x == 3 or x == 4:
                    aw = aw + " "
            if y == 5:
                if x == 0 or x == 3:
                    aw = aw + "*"
                if x == 1 or x == 2 or x == 4:
                    aw = aw + " "
            if y == 6:
                if x == 0 or x == 4:
                    aw = aw + "*"
                if x == 1 or x == 2 or x == 3:
                    aw = aw + " "
        print(aw)

# S


def s():
    for y in range(7):
        aw = ""
        for x in range(5):
            if y == 0:
                if x == 0:
                    aw = aw + " "
                if x == 1 or x == 2 or x == 3 or x == 4:
                    aw = aw + "*"
            if y == 1 or y == 2:
                if x == 0:
                    aw = aw + "*"
                if x == 1 or x == 2 or x == 3 or x == 4:
                    aw = aw + " "
            if y == 3 or y == 6:
                if x == 0 or x == 4:
                    aw = aw + " "
                if x == 1 or x == 2 or x == 3:
                    aw = aw + "*"
            if y == 4 or y == 5:
                if x == 4:
                    aw = aw + "*"
                if x == 0 or x == 1 or x == 2 or x == 3:
                    aw = aw + " "
        print(aw)

# T


def t():
    for y in range(7):
        aw = ""
        for x in range(5):
            if y == 0:
                aw = aw + "*"
            if y == 1 or y == 2 or y == 3 or y == 4 or y == 5 or y == 6:
                if x == 2:
                    aw = aw + "*"
                if x == 0 or x == 1 or x == 3 or x == 4:
                    aw = aw + " "
        print(aw)

# U


def u():
    for y in range(7):
        aw = ""
        for x in range(5):
            if y == 0 or y == 1 or y == 2 or y == 3 or y == 4 or y == 5:
                if x == 0 or x == 4:
                    aw = aw + "*"
                if x == 1 or x == 2 or x == 3:
                    aw = aw + " "
            if y == 6:
                if x == 0 or x == 4:
                    aw = aw + " "
                if x == 1 or x == 2 or x == 3:
                    aw = aw + "*"
        print(aw)

# V


def v():
    for y in range(7):
        aw = ""
        for x in range(5):
            if y == 0 or y == 1 or y == 2 or y == 3 or y == 4:
                if x == 0 or x == 4:
                    aw = aw + "*"
                if x == 1 or x == 2 or x == 3:
                    aw = aw + " "
            if y == 5:
                if x == 0 or x == 2 or x == 4:
                    aw = aw + " "
                if x == 1 or x == 3:
                    aw = aw + "*"
            if y == 6:
                if x == 0 or x == 1 or x == 3 or x == 4:
                    aw = aw + " "
                if x == 2:
                    aw = aw + "*"
        print(aw)

# W


def w():
    for y in range(7):
        aw = ""
        for x in range(5):
            if y == 0 or y == 1 or y == 2 or y == 5 or y == 6:
                if x == 0:
                    aw = aw + "*"
                if x == 1 or x == 2 or x == 3:
                    aw = aw + " "
                if x == 4:
                    aw = aw + "*"
            if y == 4:
                if x == 0 or x == 1 or x == 3 or x == 4:
                    aw = aw + "*"
                if x == 2:
                    aw = aw + " "
            if y == 3:
                if x == 1 or x == 3:
                    aw = aw + " "
                if x == 0 or x == 2 or x == 4:
                    aw = aw + "*"
        print(aw)

# X


def x():
    for y in range(7):
        aw = ""
        for x in range(5):
            if y == 0 or y == 1 or y == 5 or y == 6:
                if x == 0 or x == 4:
                    aw = aw + "*"
                if x == 1 or x == 2 or x == 3:
                    aw = aw + " "
            if y == 2 or y == 4:
                if x == 1 or x == 3:
                    aw = aw + "*"
                if x == 0 or x == 2 or x == 4:
                    aw = aw + " "
            if y == 3:
                if x == 0 or x == 1 or x == 3 or x == 4:
                    aw = aw + " "
                if x == 2:
                    aw = aw + "*"
        print(aw)

# Y


def y():
    for y in range(7):
        aw = ""
        for x in range(5):
            if y == 0 or y == 1:
                if x == 0 or x == 4:
                    aw = aw + "*"
                if x == 1 or x == 2 or x == 3:
                    aw = aw + " "
            if y == 2:
                if x == 1 or x == 3:
                    aw = aw + "*"
                if x == 0 or x == 2 or x == 4:
                    aw = aw + " "
            if y == 3 or y == 4 or y == 5 or y == 6:
                if x == 0 or x == 1 or x == 3 or x == 4:
                    aw = aw + " "
                if x == 2:
                    aw = aw + "*"
        print(aw)

# Z


def z():
    for y in range(7):
        aw = ""
        for x in range(5):
            if y == 0 or y == 6:
                aw = aw + "*"
            if y == 1:
                if x == 0 or x == 1 or x == 2 or x == 3:
                    aw = aw + " "
                if x == 4:
                    aw = aw + "*"
            if y == 2:
                if x == 0 or x == 1 or x == 2 or x == 4:
                    aw = aw + " "
                if x == 3:
                    aw = aw + "*"
            if y == 3:
                if x == 0 or x == 1 or x == 3 or x == 4:
                    aw = aw + " "
                if x == 2:
                    aw = aw + "*"
            if y == 4:
                if x == 0 or x == 2 or x == 3 or x == 4:
                    aw = aw + " "
                if x == 1:
                    aw = aw + "*"
            if y == 5:
                if x == 1 or x == 2 or x == 3 or x == 4:
                    aw = aw + " "
                if x == 0:
                    aw = aw + "*"
        print(aw)
