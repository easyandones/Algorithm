import sys


n = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(n)]
result = 4 - max(sum(1 if (data[i] + j in data) else 0 for j in range(1, 5)) for i in range(n))
print(result)
