from typing import List

class Solution:

    def get_neighbours(self, r, c, grid):
        rows = len(grid)
        cols = len(grid[0])

        neighbours = [(r+1, c+1), (r-1, c-1), (r, c+1), (r, c-1), (r+1, c), (r-1, c)]
        neighbours = [neighbour for neighbour in neighbours if 0<=neighbour[0]<=rows and 0<=neighbour[1]<=cols and grid[neighbour[0]][neighbour[1]] ==1]
        return neighbours
        
    def expand(self, r, c, grid):
        grid[r][c] == 2
        for neighbour in self.get_neighbours(r, c, grid):
            _r, _c = neighbour
            self.expand(_r, _c, grid)


    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        islands_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands_count +=1
                    self.expand(r, c, grid)
        
        return islands_count




grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]


s = Solution()
print(s.numIslands(grid))
