def firstCompleteIndex(arr: list[int], mat: list[list[int]]) -> int:
    n = len(mat)  # rows
    m = len(mat[0])  # cols
    coords = {}

    for i in range(n):
        for j in range(m):
            coords[mat[i][j]] = (i, j)

    print(coords)
    row_count = [0] * n
    column_count = [0] * m
    print(row_count)
    print(column_count)

    for k in range(len(arr)):
        r, c = coords[arr[k]]
        print(f"r: {r} and c: {c}")
        row_count[r] += 1
        column_count[c] += 1
        print(row_count)
        print(column_count)

        if column_count[c] == n or row_count[r] == m:
            return k

    # for i in range(n):
    #     for j in range(m):


print(firstCompleteIndex([1, 3, 4, 2], [[1, 4], [2, 3]]))
