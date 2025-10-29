class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        num_islands = 0

        def expand(row, col, rows, cols, grid):
            grid[row][col] = "2"
            neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            neighbors = [
                n
                for n in neighbors
                if 0 <= n[0] < rows and 0 <= n[1] < cols and grid[n[0]][n[1]] == "1"
            ]
            for n in neighbors:
                expand(n[0], n[1], rows, cols, grid)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    num_islands += 1
                    expand(row, col, rows, cols, grid)

        return num_islands
