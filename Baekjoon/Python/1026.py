import sys


n = int(sys.stdin.readline())
a = sorted(map(int, sys.stdin.readline().split()))
b = sorted(map(int, sys.stdin.readline().split()), reverse=True)
print(sum(itemA * itemB for itemA, itemB in zip(a, b)))
