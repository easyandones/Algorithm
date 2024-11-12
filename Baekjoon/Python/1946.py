import sys


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    applicants = []
    for _ in range(n):
        document, interview = map(int, sys.stdin.readline().split())
        applicants.append((document, interview))
    applicants.sort()
    count = 0
    best = n + 1
    for applicant in applicants:
        if applicant[1] < best:
            best = applicant[1]
            count += 1
    print(count)
