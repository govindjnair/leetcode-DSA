def countServers(grid: list[list[int]]) -> int:
    row = len(grid)
    column = len(grid[0])
    ans = 0
    row_count = [0] * row
    column_count = [0] * column
    for i in range(row):
        for j in range(column):
            # print(grid[i][j], end='')
            if grid[i][j] == 1:
                row_count[i] += 1
                column_count[j] += 1

    for i in range(row):
        for j in range(column):
            if grid[i][j] == 1 and (row_count[i] > 1 or column_count[j] > 1):
                ans += 1

    # print(f"row_count{row_count}")
    # print(f"column_count{column_count}")
    return ans










    # return ans

print(countServers([[1,0],[1,1]]))