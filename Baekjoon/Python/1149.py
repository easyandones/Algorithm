import sys


data = []

cache = {}
def getCases(startIndex, prevSelectedIndex=None):
    key = (startIndex, prevSelectedIndex)
    if key not in cache:
        if startIndex == len(data) - 1:
            result = min(value for index, value in enumerate(data[startIndex]) if index != prevSelectedIndex)
        else:
            result = min(getCases(startIndex + 1, index) + value for index, value in enumerate(data[startIndex]) if index != prevSelectedIndex)
        cache[key] = result
    return cache[key]

for _ in range(int(sys.stdin.readline())):
    data.append(list(map(int, sys.stdin.readline().split())))
for i in range(len(data) - 1, -1, -1):
    for j in range(3):
        getCases(i, j)
print(getCases(0))