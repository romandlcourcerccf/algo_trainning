class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        border = set()
        seen = set()
        tics = 0
        rotten = 0

        def infect():

            nonlocal border
            nonlocal seen
            nonlocal tics
            
            while len(border) > 0:
        
                _border = set()
                for p in border:

                    row, col = p[0], p[1]

                    print(f'row :{row}, col: {col}')

                    if row+1 < rows and grid[row+1][col] == 1:
                        if (row+1, col) in seen:
                             seen.remove((row+1, col))

                        _border.add((row+1, col))
                        grid[row+1][col] = 2
                        
                
                    if row-1 >=0 and grid[row-1][col] == 1:
                        if (row-1, col) in seen:
                            seen.remove((row-1, col))

                        _border.add((row-1, col))
                        grid[row-1][col] = 2
                        
                
                    if col-1 >=0 and grid[row][col-1] == 1:
                        if (row, col-1) in seen:
                            seen.remove((row, col-1))

                        _border.add((row, col-1))
                        grid[row][col-1] = 2
                        

                    if col+1 < cols and grid[row][col+1] == 1:
                        if (row, col+1) in seen:
                            seen.remove((row, col+1))

                        _border.add((row, col+1))
                        grid[row][col+1] = 2
                        

                    if row+1 < rows and col+1 < cols and grid[row+1][col+1] == 1:
                        seen.add((row+1, col+1))
                
                    if row-1 >= 0 and col-1 >= 0 and grid[row-1][col-1] == 1:
                        seen.add((row-1, col-1))
                
                    if row+1 < rows and col-1 >= 0 and grid[row+1][col-1] == 1:
                        seen.add((row+1, col-1))

                    if row-1 >= 0 and col+1 < cols and grid[row-1][col+1] == 1:
                        seen.add((row-1, col+1))

                if len(_border) > 0:
                    tics +=1 

                border = _border

        border.add((0,0))
        infect()

    
        return tics if len(seen) == 0 else -1  

            
