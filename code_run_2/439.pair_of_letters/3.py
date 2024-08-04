import sys
from collections import defaultdict

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
    # row = rows[0]


    row = 'ABCABC A'
    # row = 'AB A'
    # row = ' ABCABC A AB AB C A'
    # row = ' A BC AB     C A A   B A BC A'
    # row = '     A BC AB     C A A   B A BC A AAAAAAAAAAA    '
    words = row.split(' ')
    h = defaultdict(int)

    for w in words:
        if len(w) >= 2:
            pos = 0
            while pos < len(w)-1:
                h[w[pos:pos+2]] +=1
                pos +=1
    

    # print(h)
    max_val = float('-inf')
    for v in h.values():
        max_val = max(max_val, v)
    
    res = []

    for k,v in h.items():
        if v == max_val:
            res.append(k)
    
    res.sort()

    print(res[-1])
   
  

if __name__ == '__main__':
    main()