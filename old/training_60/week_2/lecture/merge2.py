from typing import List

a = [3, 7, 8, 9, 8]
b = [2, 4, 8]


def merge(nums1: List[int], nums2: List[int]) -> List[int]:
    merged = [0] * (len(nums1) + len(nums2))
    first1 = first2 = 0

    for k in range(len(nums1) + len(nums2)):
        print(f"f1 : {first1} f2 : {first2}")
        if (
            first1 != len(nums1)
            and first2 == len(nums2)
            or nums1[first1] <= nums2[first2]
        ):
            merged[k] = nums1[first1]
            first1 += 1
        else:
            merged[k] = nums2[first2]
            first2 += 1

    print(merged)


merge(a, b)
