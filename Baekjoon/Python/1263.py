import sys


n = int(sys.stdin.readline())
data = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

def checkSchedule(data) -> int:
    schedule = [False for _ in range(1000000)]
    for item in data:
        duration = item[0]
        deadline = item[1] - 1
        while duration > 0:
            if deadline < 0:
                return -1
            if schedule[deadline]:
                deadline -= 1
            else:
                schedule[deadline] = True
                duration -= 1
    return schedule.index(True)

print(checkSchedule(data))
