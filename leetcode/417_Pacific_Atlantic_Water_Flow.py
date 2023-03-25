class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def flow_down(row, col):

            nonlocal pas_coast
            nonlocal atl_coast

            if row == 0 and col == cols-1:
                pas_coast+=1
                atl_coast+=1
                return
            
            if row == rows-1 and col == 0:
                pas_coast+=1
                atl_coast+=1
                return

            if row == 0 or col == 0:
                pas_coast+=1
                return
            if row == rows-1 or col == cols-1:  
                atl_coast+=1
                return 
            
            if heights[row][col] >= heights[row-1][col]:
                flow_down(row-1,col)
            if heights[row][col] >= heights[row+1][col]:
                flow_down(row+1,col)
            if heights[row][col] >= heights[row][col+1]:
                flow_down(row+1,col+1)
            if heights[row][col] >= heights[row][col-1]:
                flow_down(row+1,col-1)

        rows, cols = len(heights), len(heights[0])

        res = []
        for row in range(rows):
            for col in range(cols):
                pas_coast = 0
                atl_coast = 0
                flow_down(row, col)
                if pas_coast > 0 and atl_coast > 0:
                    res.append([row, col])
       
       

        return res