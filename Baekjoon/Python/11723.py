import sys

data = [False for _ in range(20)]

for _ in range(int(sys.stdin.readline())):
    inputString = sys.stdin.readline()
    try:
        command, value = inputString.split()
        index = int(value) - 1
    except:
        command = inputString.strip()
        index = None
    if command == "add":
        data[index] = True
    elif command == "remove":
        data[index] = False
    elif command == "check":
        print(1 if data[index] else 0)
    elif command == "toggle":
        data[index] = not data[index]
    elif command == "all":
        data = [True for _ in range(20)]
    elif command == "empty":
        data = [False for _ in range(20)]