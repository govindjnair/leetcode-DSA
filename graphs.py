from collections import defaultdict, deque

n = 8

# Array of Edges (Directed) [Start, End]
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

# converting array of edges into an adjacency matrix

M = []
for i in range(n):
    M.append([0] * n)

for u, v in A:
    M[u][v] = 1
    # M[v][u] = 1 uncomment for making the graph undirected

# converting array of edges into an adjacency list


D = defaultdict(list)

for u, v in A:
    D[u].append(v)
    # D[v].append(u)

# print(M)
print(D)

# DFS with Recursion - O(V + E) where V is the number of nodes and E is the number of edges

source = 0
seen = set()
seen.add(source)


def dfs_recursion(node):
    print(node)
    for neighbour_node in D[node]:
        if neighbour_node not in seen:
            seen.add(neighbour_node)
            dfs_recursion(neighbour_node)


# dfs_recursion(source)

# Iterative DFS with Stack - O(V + E)

start = 0
seen = set()
seen.add(start)
stack = [start]

while stack:
    node = stack.pop()
    print(node)
    for neighbour_node in D[node]:
        if neighbour_node not in seen:
            seen.add(neighbour_node)
            stack.append(neighbour_node)

# BFS (Queue) - O(V + E)

source = 0
seen.add(source)
q = deque()
q.append(source)

while q:
    node = q.popleft()
    print(node)
    for neighbour_node in D[node]:
        if neighbour_node not in seen:
            seen.add(neighbour_node)
            q.append(neighbour_node)


class Node:
    def __init__(self, value):
        self.value = value
        self.neighbours = []

    def __str__(self):
        return f"Node: {self.value}"

    def display(self):
        connections = [neighbour.value for neighbour in self.neighbours]
        return f"{self.value} is connected to {connections}"


A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')

A.neighbours.append(B)
B.neighbours.append(A)

C.neighbours.append(D)
D.neighbours.append(C)

print(C.display())




