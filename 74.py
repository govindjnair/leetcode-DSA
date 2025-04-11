def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    # for row in matrix:
    #     L = 0
    #     R = len(row) - 1
    #     while L <= R:
    #         M = (L + R) // 2
    #         if row[M] == target:
    #             return True
    #         elif row[M] > target:
    #             R = M - 1
    #         else:
    #             L = M + 1
    #
    # return False
    # Time complexity is O(M.logN)

    m = len(matrix)
    n = len(matrix[0])
    t = m*n
    L = 0
    R = t - 1

    while L <= R:
        M = (L+R) // 2
        i = M // n
        j = M % n

        mid_num = matrix[i][j]
        if mid_num == target:
            return True
        elif mid_num > target:
            R = M - 1
        else:
            L = M + 1

    return False



print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
