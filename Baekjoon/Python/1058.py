import sys


n = int(sys.stdin.readline())

data = [list(item == "Y" for item in sys.stdin.readline().strip()) for _ in range(n)]
friends = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if data[i][j] == True:
            friends[i][j] = True
            for k in range(n):
                if data[j][k] == True:
                    friends[i][k] = True

count = [max(sum(1 if item else 0 for item in friends[i]) - 1, 0) for i in range(n)]
print(max(count))
