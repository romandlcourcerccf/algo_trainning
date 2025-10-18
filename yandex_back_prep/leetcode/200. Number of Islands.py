class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        islands_count = 0

        def get_neighbours(row, col, cols, rows):

            n_points = [
                (row, col),
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ]

            n_points = [p for p in n_points if <p[0]]

        def fill_up(row, col):
            grid[row][col] == "2"
            neighbours = get_neighbours(row, col)
            for neighbour in neighbours:
                fill_up(neighbour[0], neighbour[1])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands_count += 1
