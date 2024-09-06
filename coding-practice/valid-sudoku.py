class Solution(object):
    def isValidSudoku(self, board):
        # 07 - 40
        row_checks = dict()
        col_checks = dict()
        box_checks = dict()

        for row in range(9):
            if row not in row_checks:
                row_checks[row] = set()
            for col in range(9):
                if col not in col_checks:
                    col_checks[col] = set()
                if (row // 3, col // 3) not in box_checks:
                    box_checks[(row // 3, col // 3)] = set()
                if board[row][col] == '.':
                    continue
                if board[row][col] in row_checks[row] or board[row][col] in col_checks[col] or board[row][col] in box_checks[(row // 3, col // 3)]:
                    return False
                row_checks[row].add(board[row][col])
                col_checks[col].add(board[row][col])
                box_checks[(row // 3, col // 3)].add(board[row][col])
        return True
