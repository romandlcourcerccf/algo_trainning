class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, max_len = 0, 0
        h = defaultdict(int)

        for r in range(len(s)):
            h[s[r]] = 1 + h[s[r]]

            while (r - l + 1) - max(h.values()) > k:
                h[s[l]] -= 1
                l += 1

            max_len = max(r - l + 1, max_len)

        return max_len
