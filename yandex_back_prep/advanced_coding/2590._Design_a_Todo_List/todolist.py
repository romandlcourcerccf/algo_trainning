from typing import List, Dict


class TodoList:
    def __init__(self):
        self.user_id_tast_id_map = {}

    def addTask(
        self, userId: int, taskDescription: str, dueDate: int, tags: List[str]
    ) -> int:
        if userId not in self.user_id_tast_id_map:
            self.user_id_tast_id_map[userId] = []

        self.user_id_tast_id_map[userId].append([taskDescription, dueDate, tags, False])

        return len(self.user_id_tast_id_map[userId])

    def getAllTasks(self, userId: int) -> List[str]:
        if userId not in self.user_id_tast_id_map:
            return []

        return [task[0] for task in self.user_id_tast_id_map[userId] if not task[3]]

    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
        return [task[0] for task in self.user_id_tast_id_map[userId] if tag in task[2]]

    def completeTask(self, userId: int, taskId: int) -> None:
        self.user_id_tast_id_map[userId][taskId - 1][3] = True
