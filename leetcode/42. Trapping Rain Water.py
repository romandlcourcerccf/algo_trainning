class Solution:
    def trap(self, height: List[int]) -> int:
        
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        res = [0] * len(height)

        for i in range(1,len(height)-1):
            max_left[i] = max(height[i], height[i-1], max_left[i-1])

        for i in range(len(height)-2, -1, -1):
            max_right[i] = max(height[i], max_right[i+1], height[i+1])

        for i in range(len(height)):

            depth = min(max_left[i], max_right[i])
        
            if depth >= height[i]:
                res[i] = depth-height[i]
            else:
                res[i] = 0

        return sum(res)
