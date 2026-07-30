import random


# bad solution
class RandomizedSet:
    def __init__(self):
        self.s = set()

    def insert(self, val: int) -> bool:
        if val not in self.s:
            self.s.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.s:
            self.s.remove(val)
            return True

        return False

    def getRandom(self) -> int:
        return random.choice(tuple(self.s))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


import random


class RandomizedSet:
    def __init__(self):
        self.h = {}
        self.a = []

    def insert(self, val: int) -> bool:
        if val not in self.h:
            self.h[val] = len(self.a)
            self.a.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.h:
            if self.h[val] == len(self.a) - 1:
                self.a.pop()
                del self.h[val]
            else:
                self.h[val], self.a[len(self.a) - 1] = (
                    self.a[len(self.a) - 1],
                    self.h[val],
                )
                self.a.pop()
            return True

        return False
