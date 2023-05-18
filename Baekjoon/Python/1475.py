import sys
import math

charCount = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for char in sys.stdin.readline().strip():
    num = int(char)
    if num == 9:
        num = 6
    charCount[num - 1] += 1
charCount[5] = math.ceil(charCount[5] / 2)
print(max(charCount))