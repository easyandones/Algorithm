import sys


cache = [0, 1, 3]

def getResult(n):
    while len(cache) <= n:
        cache.append((getResult(n - 1) + (2 * getResult(n - 2))) % 10007)
    return cache[n]

print(getResult(int(sys.stdin.readline())))
