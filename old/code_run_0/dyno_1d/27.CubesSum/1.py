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
        "/Users/romanroman/projects/algo_trainning/code_run_0/dyno_1d/27.CubesSum/1.txt",
        "r",
    ) as f:
        rows = f.readlines()

    num = int(rows[0])

    print(num)
    min_squre, min_num = 1, 1

    dp = [0] * (num + 1)
    dp[min_squre] = 1

    for n in range(1, num + 1):
        print("n :", n)

        q_root = n ** (1 / 3)
        if q_root % 1 == 0:
            min_squre, min_num = n, 1
            dp[n] = 1
        else:
            split = n // min_squre
            tail = n % min_squre

            print("n :", n, " split :", split, " tail :", tail)
            if tail == 0:
                print(dp)

                nun_squares = dp[min_squre] * split
                print("n :", n, " nun_squares :", nun_squares)
                dp[n] = nun_squares

                if nun_squares < min_squre:
                    min_squre, min_num = num, nun_squares

            else:
                nun_squares = dp[min_squre] * split + dp[tail]
                dp[n] = nun_squares
                if nun_squares < min_squre:
                    min_squre, min_num = num, nun_squares

            print(">>>")
            print("n: ", n)
            print(dp)
            print("n :", n, " min_squre :", min_squre, "min_num :", min_num)


if __name__ == "__main__":
    main()
