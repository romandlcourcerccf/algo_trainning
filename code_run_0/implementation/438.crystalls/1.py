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

    # rows = sys.stdin.readlines()

    with open(
        "/Users/romanroman/projects/algo_trainning/code_run_0/implementation/438.crystalls/1.txt",
        "r",
    ) as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]

    crystalls = rows

    print("crystalls", crystalls)

    p1, p2, p3 = 0, 0, 0

    while (
        p1 != len(crystalls[0]) - 1
        and p2 != len(crystalls[1]) - 1
        and p3 != len(crystalls[1]) - 1
    ):
        if crystalls[0][p1] == crystalls[1][p2] == crystalls[2][p3]:
            p1 += 1
            p2 += 1
            p3 += 1

        else:
            print(f"p1 {p1} {crystalls[0][p1]}")
            print(f"p2 {p2} {crystalls[1][p2]}")
            print(f"p3 {p3} {crystalls[2][p3]}")

            h = defaultdict(int)

            h[crystalls[0][p1]] += 1
            h[crystalls[1][p2]] += 1
            h[crystalls[2][p3]] += 1

            max_smb = ""
            max_pos = float("inf")

            for i in range(h.keys()):
                if h[h.keys()[i]] < max_pos:
                    max_pos = h.keys()[i]
                    max_smb = h.keys()[i]

            break


if __name__ == "__main__":
    main()
