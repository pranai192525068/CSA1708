
from collections import deque

start = (3, 3, 0)
goal = (0, 0, 1)
moves = [(1, 0), (2, 0), (0, 1),
         (0, 2), (1, 1)]

def valid(m, c):
    return (0 <= m <= 3 and 0 <= c <= 3 and
            (m == 0 or m >= c) and
            (3-m == 0 or 3-m >= 3-c))

queue = deque([(start, [start])])
visited = {start}

while queue:
    state, path = queue.popleft()

    if state == goal:
        for s in path:
            print(s)
        break

    m, c, boat = state

    for dm, dc in moves:
        if boat == 0:
            nxt = (m-dm, c-dc, 1)
        else:
            nxt = (m+dm, c+dc, 0)

        if valid(nxt[0], nxt[1]) and nxt not in visited:
            visited.add(nxt)
            queue.append((nxt, path + [nxt]))
