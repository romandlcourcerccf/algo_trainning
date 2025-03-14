import sys
from collections import defaultdict


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

    # with open('/Users/romanroman/projects/algo_trainning/code_run_0/dict/84.Pyramid/1.txt', 'r') as f:
    #     rows = f.readlines()

    h = defaultdict(list)

    for r in range(1, len(rows)):
        r = list(map(int, rows[r].split()))
        h[r[0]].append(r)

    for k, v in h.items():
        v.sort(key=lambda x: x[1])

    widths = list(h.keys())
    widths.sort()

    total_heighth = 0

    while widths:
        max_width = widths.pop()
        # print('max_width :', max_width)
        # print(h[max_width])
        total_heighth += h[max_width].pop()[1]

    print(total_heighth)


if __name__ == "__main__":
    main()
