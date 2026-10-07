from typing import List
import os


class Solution:
    def _get_perfect_substring_len(self, row: str) -> int:
        r, l = 0, 0
        max_len = 0

        if len(row) == 0:
            return 0

        for r in range(len(row) - 1):
            if (
                row[r] == "a"
                and row[r + 1] == "h"
                or row[r] == "h"
                and row[r + 1] == "a"
            ):
                max_len = max(max_len, r - l + 1)
            else:
                l = r

        return max_len

    def get_solution(self, row: str) -> int:
        row = "@" + row + "@"

        max_len_1 = self._get_perfect_substring_len(row)
        max_len_2 = self._get_perfect_substring_len(row[::-1])

        max_len = max(max_len_1, max_len_2)

        if max_len == 0 and ("h" in row or "a" in row):
            max_len = 1

        return max_len


def read_file(path: str) -> List[str]:
    with open(os.path.join(os.path.dirname(__file__), path), "r") as reader:
        lines = reader.readlines()
        return lines


if __name__ == "__main__":
    lines = read_file("input.txt")
    row = lines[1]
    s = Solution()
    print(s.get_solution(row))
