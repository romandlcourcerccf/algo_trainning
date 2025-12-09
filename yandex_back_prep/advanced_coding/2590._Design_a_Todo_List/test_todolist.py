from todolist import TodoList

import pytest


def test_dodolist():
    todoList = TodoList()

    assert todoList.addTask(1, "Task1", 50, []) == 1
    assert todoList.addTask(1, "Task2", 100, ["P1"]) == 2

    assert todoList.getAllTasks(1) == ["Task1", "Task2"]

    assert todoList.getAllTasks(5) == []

    assert todoList.addTask(1, "Task3", 30, ["P1"]) == 3

    assert todoList.getTasksForTag(1, "P1") == sorted(["Task3", "Task2"])

    with pytest.raises(Exception):
        todoList.completeTask(5, 1)

    todoList.completeTask(1, 2)

    todoList.getTasksForTag(1, "P1") == ["Task3"]

    todoList.getAllTasks(1) == ["Task3", "Task1"]
