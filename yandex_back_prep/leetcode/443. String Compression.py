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
