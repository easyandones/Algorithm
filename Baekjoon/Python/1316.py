import sys

count = 0
for _ in range(int(sys.stdin.readline())):
    inputString = sys.stdin.readline().strip()
    data = [inputString[0]]
    index = 1
    while index < len(inputString):
        if inputString[index] != inputString[index - 1]:
            if inputString[index] in data:
                break
            else:
                data.append(inputString[index])
        index += 1
    else:
        count += 1
print(count)