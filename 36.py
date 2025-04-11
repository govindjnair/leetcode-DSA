from collections import defaultdict


def isValidSudoku(board: list[list[str]]) -> bool:
    columns = defaultdict(set)
    rows = defaultdict(set)
    squares = defaultdict(set)  # key (r/3, c/3)

    for r in range(9):  # given 9X9
        for c in range(9):
            if board[r][c] == '.':
                continue
            if board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][c] in squares[(r // 3, c // 3)]:
                return False
            rows[r].add(board[r][c])
            columns[c].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])
    print(rows)
    print(columns)
    print(squares)
    return True


print(isValidSudoku(board=
              [["5", "3", ".", ".", "7", ".", ".", ".", "."]
                  , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                  , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                  , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                  , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                  , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                  , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                  , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                  , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))


# print(isValidSudoku(board=
#                     [["8", "3", ".", ".", "7", ".", ".", ".", "."]
#                         , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
#                         , [".", "9", "8", ".", ".", ".", ".", "6", "."]
#                         , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
#                         , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
#                         , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
#                         , [".", "6", ".", ".", ".", ".", "2", "8", "."]
#                         , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
#                         , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
