import sys


n = int(sys.stdin.readline())
cranes = list(sorted(map(int, sys.stdin.readline().split()), reverse=True))

m = int(sys.stdin.readline())
boxes = list(sorted(map(int, sys.stdin.readline().split()), reverse=True))

def find() -> int:
    if boxes[0] > cranes[0]:
        return -1
    time = 0
    while len(boxes) > 0:
        time += 1
        for crane in cranes:
            if crane < boxes[-1]:
                continue
            for index in range(len(boxes)):
                if crane >= boxes[index]:
                    boxes.pop(index)
                    break
            if len(boxes) == 0:
                break
    return time

print(find())
