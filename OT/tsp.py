import sys
from itertools import permutations

def tsp():
    print("Enter the number of cities:")
    n = int(input())
    graph = {}
    cities = []

    print("Enter the city names (one per line):")
    for _ in range(n):
        city = input().strip()
        cities.append(city)
        graph[city] = {}

    print("Enter the distance matrix (row-wise, space-separated):")
    for i in range(n):
        distances = list(map(int, input().split()))
        for j in range(n):
            graph[cities[i]][cities[j]] = distances[j]

    print("Enter the starting city:")
    start = input().strip()

    nodes = list(graph.keys())
    nodes.remove(start)
    min_path = None
    min_cost = sys.maxsize

    for perm in permutations(nodes):
        current_cost = 0
        current_node = start
        for node in perm:
            current_cost += graph[current_node][node]
            current_node = node
        current_cost += graph[current_node][start]

        if current_cost < min_cost:
            min_cost = current_cost
            min_path = (start,) + perm + (start,)

    print("\nOptimal Path:", " -> ".join(min_path))
    print("Minimum Cost:", min_cost)

tsp()
