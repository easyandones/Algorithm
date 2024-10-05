import sys


n = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(n)]
if n < 3:
    print(sum(data))
    exit()
cache = [data[0], data[0] + data[1], max(data[0], data[1]) + data[2]]

def getResult(n):
    if len(cache) <= n:
        cache.append(max(getResult(n - 3) + data[n - 1], getResult(n - 2)) + data[n])
    return cache[n]

for i in range(n - 1):
    getResult(i)
print(getResult(n - 1))
