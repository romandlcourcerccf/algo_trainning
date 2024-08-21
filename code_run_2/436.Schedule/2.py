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


    # rows = []
    # rows.append('4')
    # rows.append('3 5')
    # rows.append('2 7')
    # rows.append('3 9')
    # rows.append('2 8')


    days_s = set()

    tasks = []

   
    for i in range(1, len(rows)):
        row = rows[i].split()
        row = list(map(int, row))
        l_day, s_level = row[0], row[1]
      
        tasks.append((l_day, s_level))
        days_s.add(l_day)
        
    tasks = set(tasks)
    days = max(days_s)
   
    done_tasks = []
    for d in range(1,days+1):
        pos_tasks = [t for t in tasks if t[0] >= d]
        if pos_tasks:
            pos_tasks.sort(key=lambda x: [x[0],x[1]])
            
            print(f'day {d} pos_tasks {pos_tasks}')
            print(f'day : {d} task_to_solve {pos_tasks[0]}')
            done_tasks.append(pos_tasks[0])

            tasks.remove(pos_tasks[0])

    rem_tasks = tasks - set(done_tasks)
    rem_stress = sum([t[1] for t in list(rem_tasks)])
    print(rem_stress)

if __name__ == '__main__':
    main()