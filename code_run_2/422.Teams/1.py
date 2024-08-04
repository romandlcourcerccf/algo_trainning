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

    A = int(rows[0])
    B = int(rows[1])
    N = int(rows[2])

    # rows = []
    # rows.append('10')
    # rows.append('8')
    # rows.append('2')

    # rows = []
    # rows.append('3')
    # rows.append('10')
    # rows.append('3')


    A = int(rows[0])
    B = int(rows[1])
    N = int(rows[2])

    A_divs = []
    B_divs = []

    for i in range(1,N+1):
        if A % i == 0:
            A_divs.append(i)
    
        if B % i == 0:
            B_divs.append(i)
    

    A_interval = []
    B_interval = []

    A_interval += [int(A/A_divs[-1]), A]
    B_interval += [int(B/B_divs[-1]), B]

    # print(A_interval)
    # print(B_interval)

    if A_interval[-1] < B_interval[0]:
        print('No')
    else:
        print('Yes')
        

if __name__ == '__main__':
    main()
