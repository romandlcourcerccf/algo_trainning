from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = defaultdict(int)

        for n in nums:
            h[n] += 1

        lin_h = [(k, v) for k, v in h.items()]

        lin_h.sort(key=lambda x: x[1])

        return lin_h[-1][0]

    # Boyer Moore Majority Vote Algorithm

    # https://www.youtube.com/watch?v=gY-I8uQrCkk
