class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()

        nums.sort()

        for a in range(len(nums)):
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            for i in range(a + 1, len(nums)):
                l, r = i + 1, len(nums) - 1

                while l < r:
                    if nums[a] + nums[i] + nums[l] + nums[r] < target:
                        l += 1
                    elif nums[a] + nums[i] + nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        res.add((nums[a], nums[i], nums[l], nums[r]))
                        l += 1
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1

        return [[s[0], s[1], s[2], s[3]] for s in res]
