import sys


n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

data = list(sorted(map(int, sys.stdin.readline().split())))
diff = [data[index + 1] - data[index] for index in range(len(data) - 1)]
sortedDiff = list(sorted(diff, reverse=True))

print(sum(sortedDiff[k - 1:]))
