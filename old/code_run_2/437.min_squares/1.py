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

    rows = []
    rows.append("3 5")
    # rows.append('1 1 0 0 0')
    # rows.append('1 1 1 1 1')
    # rows.append('0 0 0 1 1')

    rows.append("1 1 1 1 0")
    rows.append("1 1 0 1 1")
    rows.append("1 1 1 1 1")

    dim = list(map(int, rows[0].split()))

    rows_num, cols_num = dim[0], dim[1]
    print("cols :", cols_num)
    print("rows :", rows_num)

    arr = []
    for i in range(1, rows_num + 1):
        arr.append(list(map(int, rows[i].split())))

    print(arr)

    def _print_arr(arr):
        for r in arr:
            print(r)

    max_site = float("-inf")
    for row in range(rows_num):
        for col in range(cols_num):
            if arr[row][col] == 1:
                print(f"row: {row} col {col}")

                clear = True
                site = 1

                print("before")
                _print_arr(arr)

                for i in range(0, site + 1):
                    arr[row + i][col + site] = 2
                    print("i :", i)

                for i in range(0, site + 1):
                    arr[row + site][col + i] = 2
                    print("i :", i)

                # while clear and site < min(rows_num-row, cols_num-col):
                #     print('site :',site)
                #     for i in range(0, site):
                #         if arr[row+i][col+site] == 1:
                #             arr[row+i][col+site] = 2

                #         elif arr[row+i][col+site] == 0:
                #             clear = False
                #             break

                #     # for i in range(0, site):
                #     #     if arr[row+site][col] != 1:
                #     #         arr[row+site][col+i] = 2
                #     #         clear = False
                #     #         break
                #     if clear:
                #         site +=1

                print("afrer")
                _print_arr(arr)

                max_site = max(max_site, site)
            break

    print("max_site =", max_site)


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
