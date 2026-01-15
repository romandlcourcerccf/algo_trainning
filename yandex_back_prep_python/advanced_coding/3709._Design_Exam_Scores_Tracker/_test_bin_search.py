_times = [1, 5, 10, 20]


def _get_closest_index(time):
    l, r = 0, len(_times) - 1

    while l < r:
        print(f"l {l} r {r}")

        m = (l + r + 1) // 2
        if _times[m] == time:
            return m
        elif _times[m] < time:
            l = m
        else:
            r = m - 1

    return min(l, r), max(l, r)


# def _get_closest_index(time):
#     l, r = 0, len(_times) - 1

#     while l < r:
#         print(f"l {l} r {r}")

#         m = (l + r) // 2
#         if _times[m] == time:
#             return m
#         elif _times[m] < time:
#             l = m
#         else:
#             r = m

#     return m


search_value = 3
print(
    f"seach value : {search_value} ",
    "result : ",
    _times[_get_closest_index(search_value)],
)


# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l, r = 0, len(nums) - 1

#         while l <= r:
#             med = (l + r) // 2
#             if nums[med] == target:
#                 return med
#             elif nums[med] < target:
#                 l = med + 1
#             else:
#                 r = med - 1

#         return -1
