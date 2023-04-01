class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        def get_touched(v):
            row, col = v[0], v[1] 
            res = []

            
        def get_neighbors(v):
           
            row, col = v[0], v[1] 
            res = []
            if row-1>=0 and grid[row-1][col] == 1:
                res.append((row-1, col))
            if col-1>=0 and grid[row][col-1] == 1:
                res.append((row, col-1))
            if col+1<=cols-1 and grid[row][col+1] == 1:
                res.append((row, col+1))
            if row+1<=rows-1 and grid[row+1][col] == 1:
                res.append((row+1, col))
            return res
    
        def _print():
            for r in grid:
                print(r)

        def bfs(l):
            print('l :',l)
            _l = set()
            for v in l[list(l.keys())[-1]]:
                grid[v[0]][v[1]] = 2
                neighbors = get_neighbors(v)
                _l.update(set(neighbors))
               
            if len(_l) == 0:
                return

            l[list(l.keys())[-1] + 1] = _l
            bfs(l)

        touched = set()
        l = {0:{(0,0)}}
        _print()
        bfs(l)


        return list(l.keys())[-1]
