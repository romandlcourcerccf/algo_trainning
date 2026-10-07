import sys


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
        "/Users/romanroman/projects/algo_trainning/code_run_0/two_pointers/90.stylish_clothers/1.txt",
        "r",
    ) as f:
        rows = f.readlines()

    ts = list(map(int, rows[1].split()))
    pt = list(map(int, rows[3].split()))

    # print('ts :', ts)
    # print('pt :', pt)

    ts_min, pt_min = 0, 0
    min_dist = float("inf")

    ts_i, pt_i = 0, 0
    while ts_i <= len(ts) - 1 and pt_i <= len(pt) - 1:
        # print('ts_i :', ts_i, 'pt_i :', pt_i)
        _min_dist = abs(ts[ts_i] - pt[pt_i])
        # print('_min_dist :',_min_dist)
        if _min_dist <= min_dist:
            min_dist = _min_dist
            ts_min, pt_min = ts[ts_i], pt[pt_i]

        if ts[ts_i] == pt[pt_i]:
            break

        elif ts[ts_i] < pt[pt_i]:
            ts_i += 1
        else:
            pt_i += 1

    print(ts_min, " ", pt_min)


if __name__ == "__main__":
    main()
