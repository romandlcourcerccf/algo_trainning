class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
      
        def _print(g):
            for r in grid:
                print(r)

        def get_neighbours(orange):
            
            neighbours = []

            row, col = orange[0], orange[1]

            for r in range(row-1,row+2):
                for c in range(col-1,col+2):
                    
                    if c >=0 and c < cols and r >=0 and r < rows and grid[r][c] == 1:
                        neighbours.append((r,c))
                        grid[r][c] = 2
            
            return neighbours

        _print(grid)

        if grid[0][0] != 2:
            return 0

        border = []
        border.append((0,0))
        grid[0][0] = 2

        steps = 1
        while len(border) > 0:
            print(border)
            _border = []
            for orange in border:
                neighbours = get_neighbours(orange)
                _border.extend(neighbours)

            border = _border
            steps += 1

        _print(grid)
        return steps