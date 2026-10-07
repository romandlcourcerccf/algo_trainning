# https://youtu.be/0YjdZlgf9Ig?t=3992


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for p in prerequisites:
            graph[p[0]].append(p[1])

        # print(graph)

        black = set()
        gray = set()
        is_cycle = False

        def dfs(node):
            gray.add(node)
            for v in graph[node]:
                if v in gray:
                    nonlocal is_cycle
                    is_cycle = True
                    return
                if v not in black:
                    dfs(v)
            gray.remove(node)
            black.add(node)

        for v in range(len(graph)):
            if v not in black:
                dfs(v)

        # print('is_cycle :',is_cycle)

        return not is_cycle
