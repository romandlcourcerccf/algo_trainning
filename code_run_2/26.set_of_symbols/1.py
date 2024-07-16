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
    # s1 = rows[0]
    # s2 = rows[1]

    # s1 = 'abba'  
    # s2 = 'ab'

    s1 = "accbdd"
    s2 = 'ca'

    s2 = set([c for c in s2])
    C = set(s2)

    l = 0
    max_len = float('inf')
    for r in range(len(s1)):
        part = s1[l:r+1]
       
        _C = C.copy()
        for p in part:
            if p in _C:
               _C.remove(p)

        if len(_C) == 0:
            print(part)
            max_len = min(max_len, len(part))
        else:
            l +=1
    
    print(max_len)

if __name__ == '__main__':
    main()