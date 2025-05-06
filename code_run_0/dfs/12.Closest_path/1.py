import sys
from queue import Queue


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

    # with open('/Users/romanroman/projects/algo_trainning/code_run_0/dfs/12.Closest_path/1.txt', 'r') as f:
    #     rows = f.readlines()

    # print(rows)

    adj_matrix = []
    for r in range(1, len(rows) - 1):
        adj_matrix.append(list(map(int, rows[r].split())))

    (start, finish) = list(map(int, rows[-1].split()))

    # print('start :', start, 'finish :', finish)

    # for r in adj_matrix:
    #     print(r)

    border = Queue()
    border.put(start - 1)

    counter = 0
    visited = set()

    while not border.empty():
        counter += 1

        cur_node = border.get()
        visited.add(cur_node)

        neighbours = adj_matrix[cur_node]
        for i, n in enumerate(neighbours):
            if n > 0 and i not in visited:
                if i == finish - 1:
                    print(counter)
                    return

                border.put(i)

    print("0")


if __name__ == "__main__":
    main()
