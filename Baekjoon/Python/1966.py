import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    printer = deque()
    for index, data in enumerate(sys.stdin.readline().split()):
        printer.append((index == m, int(data)))
    printed = 0
    while printed != n:
        target = printer.popleft()
        for i in range(n - printed - 1):
            if printer[i][1] > target[1]:
                printer.append(target)
                break
        else:
            printed += 1
            if target[0]:
                print(printed)
                break