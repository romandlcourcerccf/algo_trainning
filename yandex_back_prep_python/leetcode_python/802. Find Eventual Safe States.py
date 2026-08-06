from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        result = []

        nodes_state = [False] * len(graph)
        visited = [False] * len(graph)

        for i in range(len(graph)):
            if len(graph[i]) == 0:
                nodes_state[i] = True

        print(nodes_state)

        def dfs(root):

            if visited[root] is True:
                return nodes_state[root]

            visited[root] = True

            if len(graph[root]) == 0:
                nodes_state[root] = True
                return True

            if nodes_state[root] is True:
                return True

            is_safe = True
            for child in graph[root]:
                is_safe &= dfs(child)

            if is_safe:
                nodes_state[root] = True

            return is_safe

        for i in range(len(graph)):
            if nodes_state[i] is True:
                result.append(i)
            else:
                res = dfs(i)
                if res:
                    result.append(i)

        return result
