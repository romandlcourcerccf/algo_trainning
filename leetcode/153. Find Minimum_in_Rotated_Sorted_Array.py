class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def find_pivot(l, r):
            _min = float('inf') 
            while l <= r:
                if nums[l] <= nums[r]:
                    _min = min(_min, nums[l])
                    break
                    
                mid = (l+r) // 2
                _min = min(_min, nums[mid])
                if nums[mid] >= nums[l]:
                    l = mid+1
                else:
                    r = mid-1
            
            return _min

        return find_pivot(0, len(nums)-1)
