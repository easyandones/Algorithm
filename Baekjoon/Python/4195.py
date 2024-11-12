import sys


def getParent(data, name):
    temp = name
    while name != data[name]:
        name = data[name]
    data[temp] = name
    return name


t = int(sys.stdin.readline())
for _ in range(t):
    f = int(sys.stdin.readline())
    data = {}
    size = {}
    for _ in range(f):
        a, b = sys.stdin.readline().strip().split()
        if a not in data:
            data[a] = a
            size[a] = 1
        if b not in data:
            data[b] = b
            size[b] = 1
        a = getParent(data, a)
        b = getParent(data, b)
        if a != b:
            data[a] = b
            size[b] += size[a]
            size[a] = 0
        print(size[b])
