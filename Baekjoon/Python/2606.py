import sys

def getConnectedNodes(node):
    for connection in connections:
        if node in connection:
            yield connection[1 if connection[0] == node else 0]

def infectNode(node, infectedNodes):
    infectedNodes.append(node)
    for node in getConnectedNodes(node):
        if node not in infectedNodes:
            infectNode(node, infectedNodes)

n = int(sys.stdin.readline())
connections = []
for _ in range(int(sys.stdin.readline())):
    connections.append(tuple(map(int, sys.stdin.readline().split())))

infected = []
infectNode(1, infected)
print(len(infected) - 1)