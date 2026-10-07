class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def back(i, tmp):
            if i > n or len(tmp) > k:
                return

            if len(tmp) == k:
                res.append(tmp[::])
                return

            tmp.append(i + 1)
            back(i + 1, tmp)
            tmp.pop()
            back(i + 1, tmp)

        back(0, [])

        return res
