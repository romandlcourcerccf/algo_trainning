class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def dfs(row, col):
            nonlocal is_isolated
            nonlocal visited

            if (row, col) in visited:
                return 
            
            if row == 0 or row == rows-1 or col == 0 or col == cols-1:
                is_isolated = False

            visited.add((row, col))

            if row+1 <= rows-1 and board[row+1][col] == 'O':
                dfs(row+1, col)
            
            if row-1 >= 0 and board[row-1][col] == 'O':
                dfs(row-1, col)

            if col+1 <= cols-1 and board[row][col+1] == 'O':
                dfs(row, col+1)
            
            if col-1 >= 0 and board[row][col-1] == 'O':
                dfs(row, col-1)

        def _print():
            for r in range(rows):
                print(board[r])


        # _print()   
        # print('\n')   
        _visited = set()
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O' and (row,col) not in _visited:
                    print('start :', 'row :', row, 'col :', col)
                    visited = set()
                    is_isolated = True
                    dfs(row, col)
                    # print(visited)
                    # print(is_isolated)
                    if is_isolated:
                        
                        for p in visited:
                           board[p[0]][p[1]] = 'X' 
                    _visited.update(visited)
        # _print()
