class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        res, n = 0, len(s)
        counter = defaultdict(int)
        j = 0

        for i in range(n):
            counter[s[i]] += 1
            while len(counter) > 2:
                counter[s[j]] -= 1
                if counter[s[j]] == 0:
                    counter.pop(s[j])

                j += 1

            res = max(res, i - j + 1)

        return res
