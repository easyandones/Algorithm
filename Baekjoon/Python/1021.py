import sys

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

currentIndex = 1
moved = 0
for _ in range(m):
    targetIndex = data.pop(0)
    moved += min(abs(currentIndex - targetIndex), n - abs(currentIndex - targetIndex))
    currentIndex = 1 if targetIndex == n else targetIndex
    n -= 1
    data = [index - 1 if index > targetIndex else index for index in data]
print(moved)