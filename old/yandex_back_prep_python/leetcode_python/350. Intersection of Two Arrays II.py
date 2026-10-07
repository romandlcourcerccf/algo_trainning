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


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        result = []

        nums1.sort()
        nums2.sort()

        p1, p2 = 0, 0

        while p1 <= len(nums1) - 1 and p2 <= len(nums2) - 1:
            if nums1[p1] == nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1

        return result
