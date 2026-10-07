import sys
from queue import Queue
from typing import List, Tuple


class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def fill_up(root, val: Tuple[int, int], depth: int, depths: List[int]):
    if val[0] < root.val:
        if root.left:
            fill_up(root.left, val, depth + 1, depths)
        else:
            root.left = TreeNode(val[0])
            depths[val[1]] = depth
            return
    elif val[0] > root.val:
        if root.right:
            fill_up(root.right, val, depth + 1, depths)
        else:
            root.right = TreeNode(val[0])
            depths[val[1]] = depth
            return


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

    rows = sys.stdin.readlines()

    # with open('/Users/romanroman/projects/algo_trainning/code_run_0/binary_search_tree/120.height/1.txt', 'r') as f:
    #     rows = f.readlines()

    numbers = list(map(int, rows[0].split()))
    depths = [0] * (len(numbers))

    root = None
    for i in range(len(numbers)):
        if i == 0:
            root = TreeNode(val=numbers[i])
            depths[0] = 1
        else:
            fill_up(root=root, val=(numbers[i], i), depth=2, depths=depths)

    depths = depths[:-1]
    depths = list(map(str, depths))
    print(" ".join(depths))


if __name__ == "__main__":
    main()
