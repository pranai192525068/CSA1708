
import heapq

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}

heuristic = {
    'A': 4,
    'B': 3,
    'C': 1,
    'D': 0
}

def astar(start, goal):
    pq = [(heuristic[start], 0, start, [start])]
    best = {start: 0}

    while pq:
        f, cost, node, path = heapq.heappop(pq)

        if node == goal:
            return path, cost

        if cost != best[node]:
            continue

        for neighbour, weight in graph[node].items():
            new_cost = cost + weight

            if new_cost < best.get(neighbour, float("inf")):
                best[neighbour] = new_cost
                new_f = new_cost + heuristic[neighbour]
                heapq.heappush(
                    pq,
                    (new_f, new_cost, neighbour,
                     path + [neighbour])
                )

    return None, float("inf")

path, cost = astar('A', 'D')
print("Shortest path:", path)
print("Total cost:", cost)
