
from itertools import permutations

dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(dist)
best_cost = float("inf")
best_path = None

for order in permutations(range(1, n)):
    path = (0,) + order + (0,)
    cost = sum(
        dist[path[i]][path[i+1]]
        for i in range(n)
    )

    if cost < best_cost:
        best_cost = cost
        best_path = path

print("Best route:", best_path)
print("Minimum cost:", best_cost)
