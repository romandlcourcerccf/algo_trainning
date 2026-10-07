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

    # with open('/Users/romanroman/projects/algo_trainning/code_run_0/linear_search/66.two_nums_max_product/1.txt', 'r') as f:
    #     rows = f.readlines()

    numbers = list(map(int, rows[0].split()))
    numbers.sort()

    if numbers[0] >= 0 and numbers[-1] >= 0:
        print(numbers[-2], " ", numbers[-1])
    elif numbers[0] <= 0 and numbers[-1] <= 0:
        print(numbers[0], " ", numbers[1])
    elif numbers[0] <= 0 and numbers[-1] >= 0:
        if numbers[0] * numbers[1] >= numbers[-2] * numbers[-1]:
            print(numbers[0], " ", numbers[1])
        else:
            print(numbers[-2], " ", numbers[-1])


if __name__ == "__main__":
    main()
