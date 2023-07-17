class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        cols = len(grid)
        rows = len(grid[0])

        def infect(point):
            infected, suspects = set(), set()
            x,y = point[0], point[1]

            left, right = max(x-1, 0),  min(x+1, cols)
            up, down = max(y-1, 0),  min(y+1, rows)

            if grid[left][y] == 1:
                grid[left][y] = 2
                infected.add((left, y))
            
            if grid[right][y] == 1:
                grid[right][y] = 2
                infected.add((right, y))

            if grid[x][up] == 1:
                grid[x][up] = 2
                infected.add((x, up))

            if grid[x][down] == 1:
                grid[x][down] = 2
                infected.add((x, down))

            if grid[left][up] == 1:
                suspects.add((left, up))

            if grid[right][up] == 1:
                suspects.add((right, up))

            if grid[left][down] == 1:
                suspects.add((left, down))

            if grid[right][down] == 1:
                suspects.add((right, down))

            return infected, suspects

        def bfs(start):

            border = set()
            suspects = set()
            border.add(start)

            visited = set()

            ticks = 0
            while border:
                ticks += 1
                _border = set()
                _suspects = set()
                for node in border:
                    __infected, __suspects = infect(node)
                    _border = _border | __infected
                    _suspects = _suspects | __suspects
                
                border = _border
                visited = visited | _border
                suspects = suspects | _suspects
                

            
            return ticks

        ticks = bfs((0,0))

        return ticks
                