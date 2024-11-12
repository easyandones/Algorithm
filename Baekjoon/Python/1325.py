import sys
import collections


n, m = map(int, sys.stdin.readline().split())

nodes = [[] for i in range(n)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    nodes[b - 1].append(a - 1)


best = 0
results = []
for i in range(n):
    visited = [False] * n
    queue = collections.deque([i])
    visited[i] = True
    count = 1
    while queue:
        current = queue.popleft()
        for edge in nodes[current]:
            if not visited[edge]:
                queue.append(edge)
                visited[edge] = True
                count += 1
    if count > best:
        best = count
        results = [i + 1]
    elif count == best:
        results.append(i + 1)
print(*results)
