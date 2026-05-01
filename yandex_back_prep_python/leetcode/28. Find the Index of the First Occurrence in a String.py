class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            is_same = True
            for p in range(len(needle)):
                if haystack[i + p] != needle[p]:
                    is_same = False
                    break

            if is_same:
                return i

        return -1
