import sys

totalCount = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

sortedData = []
for i in range(totalCount, 0, -1):
    sortedData.insert(data[i - 1], i)
print(" ".join(map(str, sortedData)))