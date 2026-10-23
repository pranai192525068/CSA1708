
from collections import deque

A, B = 4, 3
target = 2
start = (0, 0)

queue = deque([(start, [])])
visited = {start}

while queue:
    (x, y), path = queue.popleft()

    if x == target or y == target:
        for step in path + [(x, y)]:
            print(step)
        print("Target reached!")
        break

    pour_ab = min(x, B - y)
    pour_ba = min(y, A - x)

    states = [
        (A, y), (x, B), (0, y), (x, 0),
        (x - pour_ab, y + pour_ab),
        (x + pour_ba, y - pour_ba)
    ]

    for state in states:
        if state not in visited:
            visited.add(state)
            queue.append((state, path + [(x, y)]))
else:
    print("Target cannot be reached")
