class Solution:
    def compress(self, chars: List[str]) -> int:
        l, r, r_pos = 0, 0, 0

        while r < len(chars):
            while r < len(chars) - 1 and chars[r] == chars[r + 1]:
                r += 1

            str_len = r - l + 1

            chars[r_pos] = chars[l]
            r_pos += 1

            if str_len > 1:
                for c in str(str_len):
                    chars[r_pos] = c
                    r_pos += 1

            r += 1
            l = r

        return r_pos

    from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:

        l, r = 0, 0

        while r < len(chars):
            _l = r
            while r < len(chars) - 1 and chars[r] == chars[r + 1]:
                r += 1

            ln = r - _l + 1
            if ln == 1:
                chars[l] = chars[r]
                l += 1
            else:
                s = []

                while ln >= 1:
                    s.append(ln % 10)
                    ln = ln // 10

                chars[l] = chars[r]
                l += 1

                while s:
                    chars[l] = str(s.pop())
                    l += 1

            r += 1
        return l
