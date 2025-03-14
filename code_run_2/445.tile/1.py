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
        "/Users/romanroman/projects/algo_trainning/code_run_2/445.tile/4.txt", "r"
    ) as f:
        rows = f.readlines()

        for i in range(len(rows)):
            rows[i] = rows[i].rstrip()

    size = rows[0]
    size = list(map(int, size.split()))

    total_tiles_number = size[0] + size[1]

    black_number = size[1]

    init_size = [1, black_number]

    while True:
        full_size = (init_size[0] + 2) * (init_size[1] + 2)
        if full_size == total_tiles_number:
            # init_size.sort(reverse=True)
            print(max(init_size) + 2, "", min(init_size) + 2)
            break

        for i in range(1, init_size[1]):
            if init_size[1] % i == 0:
                init_size = [init_size[0] * i, int(init_size[1] / i)]

    # print(f'{init_size[0]} {init_size[1]}')


if __name__ == "__main__":
    main()
