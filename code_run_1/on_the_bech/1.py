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

    def min_dist(arr):
        arr = sorted(arr)
        m = arr[0] ^ arr[1]
        for i in range(1, len(arr)):
            m = min(m, arr[i - 1] ^ arr[i])
        return m

    rows = sys.stdin.readlines()

    min_distanses = []
    for t in range(2, len(rows), 2):
        arr = rows[t].split()
        arr = [int(i) for i in arr]
        min_distanses.append(min_dist(arr))

    for m_dist in min_distanses:
        print(m_dist)


if __name__ == "__main__":
    main()
