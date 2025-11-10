from typing import List


class Solution:
    def __init__(self, lists: List[List[int]]) -> None:
        self.lists = lists
        self.rem = sum([len(l) for l in lists])

    def next(self) -> int:
        val_l = self.lists.pop(0)
        val = val_l.pop(0)
        self.rem -= 1

        if val_l:
            self.lists.append(val_l)

        return val

    def has_next(self) -> bool:
        return self.rem > 0
