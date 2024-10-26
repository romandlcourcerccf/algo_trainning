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
    filename = os.path.join(dname, '1.txt')
    
    with open(filename, 'r') as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]

    A, B, C, D = int(rows[0]), int(rows[1]), int(rows[2]), int(rows[3])

    M, N = 0, 0

    if A>0 and B>0 and C > 0 and D > 0:
        if A < B and C < D or A > B and C > D:
            M = min(A,B)+1
            N = min(C,D)+1
        elif A < B and C > D or A > B and C < D:
            pass
    elif A == 0 or B == 0 or  C == 0 or D == 0:
        M, N = 1,1
       
    
    print(f'{M} {N}')
   
if __name__ == '__main__':
    main()
