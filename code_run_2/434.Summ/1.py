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

    with open('/Users/romanroman/projects/algo_trainning/code_run_2/430.pair_codes/1.txt', 'r') as f:
        rows = f.readlines()

        for i in range(len(rows)):
            rows[i] = rows[i].rstrip()

    numbers = rows[1].split()
    # print(numbers)
    pairs_count = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if set(numbers[i]) &  set(numbers[j]):
                pairs_count +=1
                
    print(pairs_count)

if __name__ == '__main__':
    main()