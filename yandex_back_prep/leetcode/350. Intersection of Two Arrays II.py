class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        c1 = Counter(nums1)
        c2 = Counter(nums2)

        intersect = list(set(nums1) & set(nums2))

        for i in range(len(intersect)):
            num_up = min(c1[intersect[i]], c2[intersect[i]])
            res += [intersect[i]] * num_up

        return res
