class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        border = []
        watched = set()
        tics = 0
        def infect():
            nonlocal border
            while len(border) > 0:
                nonlocal tics
                tics +=1
                _border = []
                for v in border:
                    row, col = v[0], v[1]
                
                    if row+1 <= rows-1 and grid[row+1][col] == 1:
                        grid[row+1][col] = 2
                        _border.append((row+1, col))
                    if row-1 >= 0 and grid[row-1][col] == 1:
                        grid[row-1][col] = 2
                        _border.append((row-1, col))  
                    if col-1 >= 0 and grid[row][col-1] == 1:
                        grid[row][col-1] = 2
                        _border.append((row, col-1))
                    if col+1 <= cols-1 and grid[row][col+1] == 1:
                        grid[row][col+1] = 2
                        _border.append((row, col+1))   
                border = _border
        border.append((0,0))
        infect()

        return tics-1