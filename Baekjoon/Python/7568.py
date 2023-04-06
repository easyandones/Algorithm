import sys

data = [(*map(int, sys.stdin.readline().split()),) for _ in range(int(sys.stdin.readline()))]
ranks = []

for a in data:
    rank = 1
    for b in data:
        if a[0] < b[0] and a[1] < b[1]:
            rank += 1
    ranks.append(rank)
print(" ".join(map(str, ranks)))