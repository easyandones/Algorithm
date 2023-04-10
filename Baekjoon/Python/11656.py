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

data = []
inputString = sys.stdin.readline().strip()

for i in range(len(inputString)):
    data.append(inputString[i:])

for string in quickSort(data):
    print(string)