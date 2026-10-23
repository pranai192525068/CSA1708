
from collections import deque

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

queue = deque([(start, [])])
visited = {start}

while queue:
    state, path = queue.popleft()

    if state == goal:
        print("Solution found:")
        for step in path + [state]:
            print(step[:3])
            print(step[3:6])
            print(step[6:])
            print()
        break

    zero = state.index(0)
    row, col = divmod(zero, 3)

    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = row + dr, col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            pos = nr * 3 + nc
            new_state = list(state)
            new_state[zero], new_state[pos] = new_state[pos], new_state[zero]
            new_state = tuple(new_state)

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [state]))
else:
    print("No solution found.")
