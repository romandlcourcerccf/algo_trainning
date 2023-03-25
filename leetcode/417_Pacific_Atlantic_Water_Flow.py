class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])

        def flow_down(row, col):

            nonlocal pas_coast
            nonlocal atl_coast
            nonlocal visited

            if row < 0 or row > rows-1 or col < 0 or col > cols-1:
                return

            if (row, col) in visited:
                return

            if pas_coast > 0 and atl_coast > 0:
                return

            if row == 0 or col == 0:
                pas_coast +=1
            
            if col == cols-1 or row == rows-1:
                atl_coast +=1

            visited.add((row, col))

            if col+1 <= cols-1 and heights[row][col+1] <= heights[row][col]:
                flow_down(row, col+1)

            if col-1 >= 0 and heights[row][col-1] <= heights[row][col]:
                flow_down(row, col-1)

            if row+1 <= rows-1 and heights[row+1][col] <= heights[row][col]:
                flow_down(row+1, col)

            if row-1 >= 0 and heights[row-1][col] <= heights[row][col]:
                flow_down(row-1, col)


        res = []
        for row in range(rows):
            for col in range(cols):
                print(f'heights {row}:{col} = {heights[row][col]}')
                pas_coast = 0
                atl_coast = 0
                visited = set()
                flow_down(row, col)
                print('visited:', visited)
                print('pas_coast :', pas_coast, 'atl_coast :', atl_coast)
                if pas_coast > 0 and atl_coast > 0:
                    res.append([row, col])
       
        return res