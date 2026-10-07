class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        while True:
            condidate = random.choice(nums)
            if nums.count(condidate) > n // 2:
                return condidate



    # Boyer Moore Majority Vote Algorithm

    # https://www.youtube.com/watch?v=gY-I8uQrCkk
