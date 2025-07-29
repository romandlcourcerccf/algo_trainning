from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        c = Counter(nums)
        f = math.floor(len(nums)/2)

        max_count = -1
        max_val = -1

        for k,v in c.items():
            if v > max_count:
                max_count = v
                max_val = k

        return max_val

        





    # Boyer Moore Majority Vote Algorithm

    # https://www.youtube.com/watch?v=gY-I8uQrCkk
