import sys


def getCases(num):
    cases = 0
    for i in range(1, 4):
        if num - i == 0:
            return cases + 1
        else:
            cases += getCases(num - i)
    return cases

for _ in range(int(sys.stdin.readline())):
    print(getCases(int(sys.stdin.readline())))