import sys


n = int(sys.stdin.readline())

data = list(sorted((int(sys.stdin.readline()) for _ in range(n)), reverse=True))

length = -1
for i in range(len(data) - 2):
    if data[i] < data[i + 1] + data[i + 2]:
        length = data[i] + data[i + 1] + data[i + 2]
        break

print(length)
