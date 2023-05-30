import sys


def processString(string):
    return " ".join(subString[::-1] for subString in string.split())

data = sys.stdin.readline().strip()
result = []

lastTagIndex = -1
for index, value in enumerate(data):
    if value == "<":
        result.append(processString(data[lastTagIndex + 1:index]))
        lastTagIndex = None
    elif value == ">":
        lastTagIndex = index
    elif lastTagIndex != None:
        continue
    result.append(value)
if lastTagIndex != None:
    result.append(processString(data[lastTagIndex + 1:]))
print("".join(result))