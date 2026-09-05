class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        self.time_to_inform = float('-inf')

        print('headID :', headID)

        graph = defaultdict(list)

        for i in range(len(manager)):
            graph[manager[i]].append(i)

        print(graph)

        def dfs(root, time):

            self.time_to_inform = max(self.time_to_inform, time)
            
            print('self.time_to_inform >>', self.time_to_inform)

            for employee in graph[root]:
                dfs(employee, time+informTime[root])

        dfs(headID, 0)

        return self.time_to_inform


