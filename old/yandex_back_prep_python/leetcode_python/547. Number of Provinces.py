class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        number_of_provincs = 0

        is_visited = [False for _ in range(len(isConnected))]

        def dfs(root):
            is_visited[root] = True

            for node in range(len(isConnected[root])):
                if isConnected[root][node] == 1 and not is_visited[node]:
                    dfs(node)

        for i in range(len(isConnected)):
            if not is_visited[i]:
                number_of_provincs += 1
                dfs(i)

        return number_of_provincs
