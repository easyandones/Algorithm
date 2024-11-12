import sys
import collections


class Participant:
    def __init__(self, value):
        self.value = value
        self.parties = []
        self.knows = False

class Party:
    def __init__(self, value):
        self.value = value
        self.participants = []


n, m = map(int, sys.stdin.readline().split())

participants = [Participant(i) for i in range(n)]
parties = [Party(i) for i in range(m)]

for i in list(map(int, sys.stdin.readline().split()))[1:]:
    participants[i - 1].knows = True

for i in range(m):
    for j in list(map(int, sys.stdin.readline().split()))[1:]:
        parties[i].participants.append(participants[j - 1])
        participants[j - 1].parties.append(parties[i])


queue = collections.deque()
for participant in participants:
    if not participant.knows:
        continue
    queue.append(participant)
    while queue:
        current = queue.popleft()
        for party in current.parties:
            for item in party.participants:
                if not item.knows:
                    item.knows = True
                    queue.append(item)


count = 0
for party in parties:
    if any(participant.knows for participant in party.participants):
        continue
    else:
        count += 1
print(count)
