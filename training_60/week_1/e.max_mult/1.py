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

    import os
    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, '3.txt')
    
    with open(filename, 'r') as f:
        rows = f.readlines()
       
    mumbers = list(map(int,rows[0].split()))

    max1, max2 = float('-inf'), float('-inf')
    min1, min2 = float('inf'), float('inf')

    for n in mumbers:

        if n > max1:
            max1 = max2
            max2 = n
        elif n > max2:
            max2 = n
            

        if n < min1:
            min1 = min2
            min2 = n
        elif n < min2:
            min2 = n

    if max1 * max2 > min1 * min2:
        if max1 > max2:
            print(f'{max1}  {max2}')
        else:
            print(f'{max2}  {max1}')
    else:
        if min1 > min2:
            print(f'{min1}  {min2}')
        else:
            print(f'{min2}  {min1}')
    
if __name__ == '__main__':
    main()
