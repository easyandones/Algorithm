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


n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
print(sum(value * (n - index) for index, value in enumerate(quickSort(data))))