class Solution:
    def one_edit_distance(self, s: str, t: str) -> bool:
        if len(s) == len(t):  # not more one distinct char
            diff_count = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    diff_count += 1
            return diff_count <= 1

        elif len(s) == len(t) + 1:
            p1 = p2 = 0
            shift = False
            while p1 < len(s) and p2 < len(t):
                if s[p1] == t[p2]:
                    p1 += 1
                    p2 += 1

                else:
                    if shift:
                        return False
                    else:
                        p1 += 1
                        shift = True


s = Solution()

assert s.one_edit_distance("ab", "acb") == True
assert s.one_edit_distance("cab", "ad") == False
assert s.one_edit_distance("1203", "1213") == True
