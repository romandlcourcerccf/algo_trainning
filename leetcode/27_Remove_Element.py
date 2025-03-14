class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        ln = len(nums)

        for i in range(ln):
            if nums[i] == val:
                k += 1
            else:
                nums[i - k] = nums[i]

        return ln - k
