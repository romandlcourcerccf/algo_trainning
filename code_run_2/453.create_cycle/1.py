
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

    with open('/Users/romanroman/projects/algo_trainning/code_run_2/453.create_cycle/2.txt', 'r') as f:
        rows = f.readlines()
        for r in rows:
            r.rstrip()

    
    v_a  = list(map(int, rows[0].split()))
    vertices = v_a[0]
    adges = v_a[1]

    print('vertices :',vertices,'adges :', adges)

    p = vertices // 2
    print('p :',p)


    graph = defaultdict(list)
    for i in range(1, len(rows)):
        pair = list(map(int,rows[i].split()))
        s, f = pair[0], pair[1]
        graph[s].append(f)
        graph[f].append(s)

    print(graph)
if __name__ == '__main__':
    main()