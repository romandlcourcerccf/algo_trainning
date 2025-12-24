from typing import List


class RoyalMember:
    def __init__(self, name: str, is_alive: bool = True):
        self.name = name
        self.is_alive = is_alive
        self.children = []


class ThroneInheritance:
    def __init__(self, kingName: str):
        self.root = RoyalMember(name=kingName)

    def birth(self, parentName: str, childName: str) -> None:
        stack = [self.root]

        while stack:
            cur = stack.pop()
            if cur.name == parentName:
                cur.children.append(RoyalMember(name=childName))
                break

            if cur.children:
                for child in cur.children:
                    stack.append(child)

    def death(self, name: str) -> None:
        stack = [self.root]

        while stack:
            cur = stack.pop()
            if cur.name == name:
                cur.is_alive = False
                break

            if cur.children:
                for child in cur.children:
                    stack.append(child)

    def getInheritanceOrder(self) -> List[str]:
        result = []

        stack = [self.root]

        while stack:
            cur = stack.pop()
            if cur.is_alive:
                result.append(cur.name)

            if cur.children:
                for child in cur.children[::-1]:
                    stack.append(child)

        return result
