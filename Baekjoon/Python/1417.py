import sys


n = int(sys.stdin.readline())

current = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(n - 1)]

required = 0
if len(data) != 0:
    while max(data) >= current + required:
        required += 1
        data[data.index(max(data))] -= 1

print(required)
