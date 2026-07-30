class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")

        stack = []

        for p in path:
            if p != "." and p != ".." and p != "":
                stack.append(p)
            elif p == "..":
                if stack:
                    stack.pop()

        res = []
        res.append("/")
        for i, s in enumerate(stack):
            res.append(s)
            if i < len(stack) - 1:
                res.append("/")

        return "".join(res)
