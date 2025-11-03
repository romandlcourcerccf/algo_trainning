# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


class NestedIterator:
    def __init__(self, nestedList):
        self.cur_list = nestedList
        self.cur_index = 0

        self._hasNext = len(self.cur_list) > 0

        self.stack = []

    def next(self) -> int:
        if 0 <= self.cur_index <= len(self.cur_list) - 1:
            if type(self.cur_list[self.cur_index]) is not list:
                res = self.cur_list[self.cur_index]
                self.cur_index += 1
                return res
            else:
                self.stack.append((self.cur_list, self.cur_index))
                self.cur_list = self.cur_list[self.cur_index]
                self.cur_index = 0

                res = self.cur_list[self.cur_index]
                self.cur_index += 1
                return res
        else:
            if self.stack:
                self.cur_list, self.cur_index = self.stack.pop()
                if 0 <= self.cur_index <= len(self.cur_list) - 1:
                    res = self.cur_list[self.cur_index]
                    self.cur_index += 1
                    return res
                else:
                    self._hasNext = False

            else:
                self._hasNext = False

    def hasNext(self) -> bool:
        return self._hasNext


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

l = [1, [2, 3, 4], 5, 6]
print("l:", l)
ni = NestedIterator(l)

print(ni.cur_index)
print(ni.hasNext())


print(">", ni.next())
print(">", ni.next())
print(">", ni.next())
print(">", ni.next())
print(">", ni.next())
print(">", ni.next())
print("has next :", ni.hasNext())
print(">", ni.next())
print("has next :", ni.hasNext())
print(">", ni.next())
print("has next :", ni.hasNext())
