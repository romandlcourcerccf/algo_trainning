class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = float("-inf")
        area = 0

        cols = len(grid[0])
        rows = len(grid)

        def _print():
            for row in grid:
                print(row)

        def dfs(col, row):
            nonlocal area
            area += 1
            grid[row][col] = 2

            if col - 1 >= 0 and grid[row][col - 1] == 1:
                dfs(col - 1, row)

            if row - 1 >= 0 and grid[row - 1][col] == 1:
                dfs(col, row - 1)

            if row + 1 <= rows - 1 and grid[row + 1][col] == 1:
                dfs(col, row + 1)

            if col + 1 <= cols - 1 and grid[row][col + 1] == 1:
                dfs(col + 1, row)

        # _print()
        # print('\n')

        for col in range(cols):
            for row in range(rows):
                if grid[row][col] == 1:
                    area = 0
                    dfs(col, row)
                    max_area = max(max_area, area)

        # _print()
        return max_area if max_area != float("-inf") else 0
