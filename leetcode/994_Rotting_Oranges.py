class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        cols = len(grid)
        rows = len(grid[0])

        def infect(point):
            infected, suspects = set(), set()
            x, y = point[0], point[1]

            left, right = max(x - 1, 0), min(x + 1, cols)
            up, down = max(y - 1, 0), min(y + 1, rows)

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

        ticks = bfs((0, 0))

        return ticks

class Solution:
    def add_to_border(self, row: int, col: int, rows: int, cols: int, grid: List[List[int]], border :set):
        if 0<=col<cols and 0<=row<rows and grid[row][col] == 1:
            grid[row][col] = 2
            border.add((row, col))
            return 1
        return 0

    def bfs(self, grid: List[List[int]]) -> int:
        fresh_count = 0
        rows, cols = len(grid), len(grid[0])

        start_row,  start_col = -1,-1 
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh_count +=1
                elif grid[row][col] == 2 and  (start_row == -1 and start_col == -1):
                    start_row,  start_col = row, col
        
        if fresh_count == 0:
            return 0

        if start_row == -1 and start_col == -1:
            return -1

        ticks = 0
        border = set()
        border.add((start_row,start_col))
    
        affected = 0
        while border:
            _border = set()
            for p in border:
                row, col = p
                affected += self.add_to_border(row+1, col, rows, cols, grid, _border)
                affected += self.add_to_border(row-1, col, rows, cols,  grid, _border)
                affected += self.add_to_border(row, col+1, rows, cols,  grid, _border)
                affected += self.add_to_border(row, col-1, rows, cols,  grid, _border)
            ticks +=1
            border = _border

            self.print(grid)

        print('ticks : ',ticks)
        print(f'fresh_count {fresh_count} affected {affected}')

        return -1 if affected < fresh_count else ticks-1

    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # self.print(grid)
        res = self.bfs(grid)
        self.print(grid)

        return res

    def print(self, grid):
        for r in grid:
            print(r)
        print('\n')