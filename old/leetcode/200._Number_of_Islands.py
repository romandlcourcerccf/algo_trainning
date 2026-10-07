class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cols = len(grid)
        rows = len(grid[0])

        def _print():
            for row in range(rows - 1):
                print(grid[row])
            print("\n")

        def valid(t):
            c, r = t[0], t[1]
            return (
                c >= 0
                and c <= cols - 1
                and r >= 0
                and r <= rows - 1
                and grid[c][r] == "1"
            )

        def dfs(t):
            col, row = t[0], t[1]
            grid[col][row] = "2"

            left = (col - 1, row)
            if valid(left):
                dfs(left)
            right = col + 1, row
            if valid(right):
                dfs(right)
            up = col, row + 1
            if valid(up):
                dfs(up)
            down = col, row - 1
            if valid(down):
                dfs(down)

        # _print()
        islands = 0
        for col in range(cols):
            for row in range(rows):
                if grid[col][row] == "1":
                    islands += 1
                    dfs((col, row))
                    # _print()

        return islands



class Solution:

    def print(self, arr):
        for r in arr:
            print(r)

    def expand(self, row, col, grid, rows, cols):

        if not (0<=row<=rows-1 and 0<=col<=cols-1 and grid[row][col]=="1"):
            return 

        grid[row][col]="3"

        self.expand(row-1, col, grid, rows, cols)
        self.expand(row+1, col, grid, rows, cols)
        self.expand(row, col-1, grid, rows, cols)
        self.expand(row, col+1, grid, rows, cols)

    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        count = 0
    
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    count+=1
                    self.expand(row, col, grid, rows, cols)

        return count


