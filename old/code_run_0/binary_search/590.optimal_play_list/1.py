import sys
from queue import Queue
from typing import List

depths = []


class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def fill_up(root, val, depth):
    if val < root.val:
        if root.left:
            fill_up(root.left, val, depth + 1)
        else:
            root.left = TreeNode(val)
            depths.append(depth)
            return
    elif val > root.val:
        if root.right:
            fill_up(root.right, val, depth + 1)
        else:
            root.right = TreeNode(val)
            depths.append(depth)
            return


max_depth = float("-inf")


def dfs(root: TreeNode, depth: int):
    global max_depth

    if not root:
        return

    max_depth = max(max_depth, depth)

    dfs(root.left, depth + 1)
    dfs(root.right, depth + 1)


def main():
    """
    Для чтения входных данных необходимо получить их
    из стандартного потока ввода (sys.stdin).
    Данные во входном потоке соответствуют описанному
    в условии формату. Обычно входные данные состоят
    из нескольких строк.
    Можно использовать несколько методов:
    * input() -- читает одну строку из потока без символа
    перевода строки;
    * sys.stdin.readline() -- читает одну строку из потока,
    сохраняя символ перевода строки в конце;
    * sys.stdin.readlines() -- вернет список (list) строк,
    сохраняя символ перевода строки в конце каждой из них.
    Чтобы прочитать из строки стандартного потока:
    * число -- int(input()) # в строке должно быть одно число
    * строку -- input()
    * массив чисел -- map(int, input().split())
    * последовательность слов -- input().split()
    Чтобы вывести результат в стандартный поток вывода (sys.stdout),
    можно использовать функцию print() или sys.stdout.write().
    Возможное решение задачи "Вычислите сумму чисел в строке":
    print(sum(map(int, input().split())))
    """

    # rows = sys.stdin.readlines()

    with open(
        "/Users/romanroman/projects/algo_trainning/code_run_0/binary_search/590.optimal_play_list/1.txt",
        "r",
    ) as f:
        rows = f.readlines()


if __name__ == "__main__":
    main()
