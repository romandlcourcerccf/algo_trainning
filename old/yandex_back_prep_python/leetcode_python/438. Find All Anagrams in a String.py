class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []

        p_counter = Counter(p)
        s_counter = Counter(s[0 : len(p) + 1])

        for i in range(len(s) - len(p) + 1):
            if i == 0:
                s_counter = Counter(s[0 : len(p)])

            else:
                s_counter[s[i - 1]] -= 1

                if s_counter[s[i - 1]] == 0:
                    del s_counter[s[i - 1]]

                s_counter[s[i + len(p) - 1]] += 1

            if p_counter == s_counter:
                res.append(i)

        return res
