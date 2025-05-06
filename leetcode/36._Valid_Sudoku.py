class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols, rows, cells = [], [], []

        for _ in range(9):
            cols.append(set())
            rows.append(set())
            cells.append(set())

        for col in range(9):
            for row in range(9):
                num = board[col][row]

                if num == ".":
                    continue

                if num in cols[col]:
                    return False

                if num in rows[row]:
                    return False

                cell = col // 3 + row // 3

                print("col :", col, "row :", row, "cell :", cell)

                if num in cells[cell]:
                    return False

                cols[col].add(num)
                rows[row].add(num)
                cells[cell].add(num)

        for i in range(9):
            if len(cols[i]) == 0 or len(rows[i]) == 0 or len(cells[i]) == 0:
                return False

        return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
