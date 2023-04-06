import sys

x = int(sys.stdin.readline())

i = 1
while x > i:
    x -= i
    i += 1

if i % 2 == 0:
    print(f"{x}/{i + 1 - x}")
else:
    print(f"{i + 1 - x}/{x}")