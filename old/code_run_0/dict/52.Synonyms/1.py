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

    _rows = sys.stdin.readlines()

    rows = []
    for r in _rows:
        rows.append(r.rstrip())

    # print(rows)
    # with open('/Users/romanroman/projects/algo_trainning/code_run_0/dict/52.Synonyms/1.txt', 'r') as f:
    #     rows = f.readlines()

    h = defaultdict(str)

    word_to_search = rows[-1]

    for i in range(1, len(rows) - 1):
        pair = rows[i].split()
        h[pair[1]] = pair[0]
        h[pair[0]] = pair[1]

    # print(h)
    # print(word_to_search)
    # print(word_to_search in h)
    print(h[word_to_search])


if __name__ == "__main__":
    main()
