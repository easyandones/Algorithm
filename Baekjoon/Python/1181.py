import sys

def compare(stringA, stringB):
    if len(stringA) == len(stringB):
        return stringA < stringB
    else:
        return len(stringA) < len(stringB)

def quickSort(listData):
    pivot = len(listData) // 2
    if pivot == 0:
        return listData
    frontData = []
    backData = []
    for data in listData:
        if data == listData[pivot]:
            continue
        elif compare(data, listData[pivot]):
            frontData.append(data)
        else:
            backData.append(data)
    return quickSort(frontData) + [listData[pivot]] + quickSort(backData)

data = []
for _ in range(int(sys.stdin.readline())):
    newInput = sys.stdin.readline().strip()
    if newInput not in data:
        data.append(newInput)

for string in quickSort(data):
    print(string)