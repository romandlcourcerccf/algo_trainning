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

    print(rows)
    n = int(rows[0])
    m = int(rows[1])

    xs = list(map(int,rows[2].split()))
    bs = list(map(int,rows[3].split()))
    ax = [10] * n

    print('n :', n)
    print('m :', m)
    print('xs :', xs)
    print('bs :', bs)


    _bs = []
    for j in range(len(bs)):
        bi = 0
        for i in range(1, n+1):
            bi += xs[j] ** (i-1) * ax[i-1]

        bi = bi%2
        _bs.append(bi)

    
    print('_bs :', _bs)
    print('bs  :',  bs)

    comp = []
    for i in range(m):
        comp.append(_bs[i] == bs[i])


    all_equal = all(comp)
    print(all_equal)

if __name__ == '__main__':
    main()
