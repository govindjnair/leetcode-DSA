


def gridGame(grid: list[list[int]]) -> int:
        ans = float("inf")
        s1, s2 = sum(grid[0]), 0
        for index, value in enumerate(grid[0]):
            s1 -= value
            ans = min(ans, max(s1, s2))
            s2 += grid[1][index]
        return ans










print(gridGame([[2, 5, 4], [1, 5, 1]]))
