import sys

def quickSort(listData):
    pivot = len(listData) // 2
    if pivot == 0:
        return listData
    frontData = []
    middleData = []
    backData = []
    for data in listData:
        if data < listData[pivot]:
            frontData.append(data)
        elif data > listData[pivot]:
            backData.append(data)
        else:
            middleData.append(data)
    return quickSort(frontData) + middleData + quickSort(backData)


n, l = map(int, sys.stdin.readline().split())
positions = quickSort(list(map(int, sys.stdin.readline().split())))

count = 0
coveredPosition = 0
for position in positions:
    if position > coveredPosition:
        count += 1
        coveredPosition = position + l - 1
print(count)