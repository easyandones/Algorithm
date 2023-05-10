import sys

def checkBrackets(string):
    count = 0
    for char in string:
        if char == "(":
            count += 1
        elif char == ")":
            if count == 0:
                return False
            count -= 1
    return count == 0

for _ in range(int(sys.stdin.readline())):
    print("YES" if checkBrackets(sys.stdin.readline().strip()) else "NO")