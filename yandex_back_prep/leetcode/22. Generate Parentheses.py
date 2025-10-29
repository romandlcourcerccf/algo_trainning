class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def back_track(open_count, close_count):
            if open_count == close_count == n:
                res.append("".join(stack))
                return

            if open_count < n:
                stack.append("(")
                back_track(open_count + 1, close_count)
                stack.pop()

            if close_count < open_count:
                stack.append(")")
                back_track(open_count, close_count + 1)
                stack.pop()

        back_track(0, 0)

        return res
