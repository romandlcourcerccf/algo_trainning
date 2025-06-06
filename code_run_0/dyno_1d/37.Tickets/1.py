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

    # Если можно, подскажи в какую сторону мыслить в задаче 20.
    # Гистограмма и прямоугольник.
    # По тегам указано stack и linearSearch,
    # что и пытаюсь реализовать: итерирую по индексам высот столбцов и добавляю в стек
    # если пустой или высота больше вершины стека,
    # иначе если меньше,
    # то вычислю площадь и удаляю индексы из стека попутно проверяя пуст ли стек
    # и высота вершины больше текущей.
    # Вроде линейно должно быть.
    # На втором закрытом тесте ловлю w/a и не могу придумать тестовые,
    # по которым алгоритм не работает((( Буду признателен за совет!

    rows = sys.stdin.readlines()

    # with open('/Users/roman/projects/algo_trainning-1/code_run_0/dyno_1d/37.Tickets/1.txt', 'r') as f:
    #     rows = f.readlines()

    nums = int(rows[0])

    dp = [[0] * 4 for i in range(nums + 3)]

    for i in range(1, len(rows)):
        row = list(map(int, rows[i].split()))
        row.append(0)

        dp[i + 2] = row

    for i in range(3):
        for c in range(3):
            dp[i][c] = float("inf")

    for i in range(3, nums + 3):
        dp[i][3] = min(
            dp[i - 1][3] + dp[i][0],
            dp[i - 2][3] + dp[i - 1][1],
            dp[i - 3][3] + dp[i - 2][2],
        )

    print(dp[-1][-1])


if __name__ == "__main__":
    main()
