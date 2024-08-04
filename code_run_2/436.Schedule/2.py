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

    # h =defaultdict(list)
    days_s = set()

    tasks = []

    for i in range(1, len(rows)):
        row = rows[i].split()
        row = list(map(int, row))
        l_day, s_level = row[0], row[1]
      
        tasks.append((l_day, s_level))
        days_s.add(l_day)
        

    print(tasks)
    tasks = set(tasks)

    print('days_s :', days_s)

    days = max(days_s)
    print('days :', days)

    done_tasks = []
    for d in range(days):
        pos_tasks = [t for t in tasks if t[0] >= d+1]
        if pos_tasks:
            pos_tasks.sort(reverse=True, key=lambda x: x[1])

            print(f'd : {d+1} pos_tasks: {pos_tasks}')

            done_tasks.append(pos_tasks[0])
            tasks.remove(pos_tasks[0])

        
    
    print(done_tasks)

    # res = 0
    # for v in h.values():
    #     res += sum(v)
    
    # print(res)




if __name__ == '__main__':
    main()