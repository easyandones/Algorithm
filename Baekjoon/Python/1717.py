import sys


n, m = map(int, sys.stdin.readline().split())

elements = [i for i in range(n + 1)]

def getParent(index):
    temp = index
    while index != elements[index]:
        index = elements[index]
    elements[temp] = index
    return index


for i in range(m):
    operation, a, b = map(int, sys.stdin.readline().split())
    if operation == 0:
        elements[getParent(b)] = getParent(a)
    else:
        if getParent(a) == getParent(b):
            print("YES")
        else:
            print("NO")
