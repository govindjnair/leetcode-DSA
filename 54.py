def spiralOrder(matrix: list[list[int]]) -> list[int]:
    m, n = len(matrix), len(matrix[0])
    ans = []
    i, j = 0, 0
    UP, DOWN, RIGHT, LEFT = 0, 1, 2, 3
    direction = RIGHT

    UP_WALL = 0
    RIGHT_WALL = n
    DOWN_WALL = m
    LEFT_WALL = -1

    while len(ans) != m*n:
        if direction == RIGHT:
            while j < RIGHT_WALL:
                ans.append(matrix[i][j])
                j += 1
            i, j = i+1, j-1
            RIGHT_WALL -= 1
            direction = DOWN
        elif direction == DOWN:
            while i < DOWN_WALL:
                ans.append(matrix[i][j])
                i += 1
            i, j = i-1, j-1
            DOWN_WALL -= 1
            direction = LEFT
        elif direction == LEFT:
            while j > LEFT_WALL:
                ans.append(matrix[i][j])
                j -= 1
            i, j = i-1, j+1
            LEFT_WALL += 1
            direction = UP
        else:
            while i > UP_WALL:
                ans.append(matrix[i][j])
                i -= 1
            i, j = i+1, j+1
            UP_WALL += 1
            direction = RIGHT

    return ans


print(spiralOrder(matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]))




