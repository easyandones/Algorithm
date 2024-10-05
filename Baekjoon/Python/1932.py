import sys


n = int(sys.stdin.readline())

data: list[list[int]] = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cache: list[list[int | None]] = [[None for _ in range(i + 1)] for i in range(n)]


def getMax(y: int, x: int) -> int:
    if cache[y][x] is None:
        if y == n - 1:
            cache[y][x] = data[y][x]
        else:
            cache[y][x] = data[y][x] + max(getMax(y + 1, x), getMax(y + 1, x + 1))
    return cache[y][x]

print(getMax(0, 0))
