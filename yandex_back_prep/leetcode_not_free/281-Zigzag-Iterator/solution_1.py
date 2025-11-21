from typing import List


class Solution:
    def __init__(self, lists: List[List[int]]) -> None:
        self.lists = lists

    def next(self) -> int:
        if len(self.lists) > 1:
            res = self.lists[0].pop(0)
            if len(self.lists[0]) == 0:
                self.lists.pop(0)
            else:
                _tmp = self.lists.pop(0)
                self.lists.append(_tmp)
        else:
            res = self.lists[0].pop(0)
            if len(self.lists[0]) == 0:
                self.lists.pop(0)

        return res

    def has_next(self) -> bool:
        _len = 0
        for i in range(len(self.lists)):
            _len += len(self.lists[i])

        return _len > 0
