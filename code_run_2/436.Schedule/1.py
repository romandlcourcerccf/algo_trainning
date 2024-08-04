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
    rows = []
    rows.append('3')
    rows.append('1 2')
    rows.append('1 3')
    rows.append('3 1')

    h =defaultdict(list)
    days = set()

    for i in range(1, len(rows)-1):
        row = rows[i].split()
        row = list(map(int, row))
        l_day, s_level = row[0], row[1]
        h[l_day].append(s_level)
        days.add(l_day)
    
    
    days = list(days)
    days.sort()

    for d in days:
        max_stress = max(h[d])
        h[d].remove(max_stress)
    
    print(h)

    res = 0
    for v in h.values():
        res += sum(v)
    
    print(res)




if __name__ == '__main__':
    main()