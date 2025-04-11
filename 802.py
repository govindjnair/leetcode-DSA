def eventualSafeNodes(graph: list[list[int]]) -> list[int]:
    n = len(graph)
    safe = {}

    def dfs(i):
        if i in safe:
            return safe[i]
        safe[i] = False
        for neighbours in graph[i]:
            if not dfs(neighbours):
                return safe[i]
        safe[i] = True
        return safe[i]

    res = []
    for i in range(n):
        if dfs(i):
            res.append(i)

    return res


print(eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]))
