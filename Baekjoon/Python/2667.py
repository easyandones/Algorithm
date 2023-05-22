import sys

n = int(sys.stdin.readline())
mapData = [[] for i in range(n)]

def isAvailable(x, y):
    if 0 <= x < n and 0 <= y < n:
        if mapData[x][y] == (1, False):
            mapData[x][y] = (1, True)
            return True
    return False

for i in range(n):
    mapData[i] = [(int(data), False) for data in sys.stdin.readline().strip()]

complex = []
for i in range(n):
    for j in range(n):
        if isAvailable(i, j):
            complex.append(1)
            queue = [(i, j)]
            while len(queue) != 0:
                currentX, currentY = queue.pop(0)
                for checkX, checkY in [
                    (currentX - 1, currentY),
                    (currentX + 1, currentY),
                    (currentX, currentY - 1),
                    (currentX, currentY + 1)
                ]:
                    if isAvailable(checkX, checkY):
                        complex[len(complex) - 1] += 1
                        queue.append((checkX, checkY))
print(len(complex))
for data in sorted(complex):
    print(data)