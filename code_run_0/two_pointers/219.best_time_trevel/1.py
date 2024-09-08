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

    rows = sys.stdin.readlines()

    # with open('/Users/romanroman/projects/algo_trainning/code_run_0/two_pointers/219.best_time_trevel/1.txt', 'r') as f:
    #     rows = f.readlines()

    max_change = float('-inf')
    max_period = 0
    max_left = 0
    max_right = 0

    temperatures = list(map(int, rows[0].split()))

    l, r = 0, 1

    while r <= len(temperatures)-1:
        change = temperatures[r] - temperatures[l]
        period = r - l

        if change <= 0:
            l+=1
        else:
            if change > max_change:
                max_change = change
                max_period = period
                max_left = l
                max_right = r
            elif change == max_change:
                if period > max_period:
                    max_period = period
                    max_left = l
                    max_right = r
            r+=1

    print(f'{max_change} {max_left} {max_right}')


if __name__ == '__main__':
    main()
