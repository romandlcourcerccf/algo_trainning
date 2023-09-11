class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        self.is_match = False
        rows = len(board)
        cols = len(board[0])

        def get_neighbors(pos):
            row, col = pos[0], pos[1]
            up, down, left, right = max(0, row-1),  min(rows-1, row+1),  max(0, col-1),  min(cols-1, col+1)
            res = set([(up, col), (down, col), (row, left), (row, right)])
            res = res - set([pos])
            return res

        def backtrack(i, pos, path):
          
            if i >= len(word):
                return 

            if board[pos[0]][pos[1]] == word[i]:
                _path = path.copy()
               
                _path.add((pos[0],pos[1]))
                
                if i == len(word)-1:
                    self.is_match = True
                    return 

                neighbors = get_neighbors(pos)
                neighbors = neighbors - path 
               
                if neighbors:
                    for neighbor in neighbors:
                        backtrack(i+1, neighbor, _path)

        for c in range(cols):
            for r in range(rows):
                if board[r][c] == word[0]:
                    backtrack(0, (r, c), set())

        return self.is_match

