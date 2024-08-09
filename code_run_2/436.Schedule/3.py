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
    rows = sys.stdin.readlines()
    # rows = []
    # rows.append('3')
    # rows.append('1 2')
    # rows.append('1 3')
    # rows.append('3 1')


    # rows = []
    # rows.append('4')
    # rows.append('3 5')
    # rows.append('2 7')
    # rows.append('3 9')
    # rows.append('2 8')


    days_s = set()
    tasks = defaultdict(list)

   
    for i in range(1, len(rows)):
        row = rows[i].split()
        row = list(map(int, row))
        l_day, s_level = row[0], row[1]
    
        tasks[l_day].append((l_day, s_level))
        days_s.add(l_day)
        
    
    sorted_tasks = []

    for day, tsks in tasks.items():
        sorted_tasks.append((day, tsks))

    sorted_tasks.sort()
    for d in sorted_tasks:
        d[1].sort(reverse=True, key=lambda x: x[1])
    

    # print(sorted_tasks)
    # print(days_s)

    for d in range(1, max(days_s)+1):
        valid_days = [_d for _d in sorted_tasks if  _d[0] >= d] 

        for valid_day in valid_days:
            if len(valid_day[1]) > 0:
                valid_day[1].pop(0)
                break


    # print(sorted_tasks)

    total_stress = 0
    for t in sorted_tasks:
        _total_stress = t[1]
        if len(_total_stress) > 0:
            for _s in _total_stress:
                total_stress += _s[1]
    
    print(total_stress)

if __name__ == '__main__':
    main()