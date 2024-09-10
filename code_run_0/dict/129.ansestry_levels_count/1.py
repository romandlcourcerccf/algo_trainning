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

    with open('/Users/romanroman/projects/algo_trainning/code_run_0/dict/129.ansestry_levels_count/1.txt', 'r') as f:
        rows = f.readlines()

        _rows = []
        for r in rows:
            _rows.append(r.strip())
        
        rows = _rows

    h = defaultdict(str)

    names = set()
    for i, r in enumerate(rows):
        if i == 0:
            continue

        r = r.split()
      
        names.add(r[0])
        names.add(r[1])

        h[r[0]]=r[1]
    

    depths = []
    for n in names:
        depth = 0
        _n = n
        while _n in h:
            depth +=1
            _n = h[_n]
        
        depths.append((n, depth))

    depths.sort(key=lambda x: x[0])

    for d in depths:
        print(f'{d[0]} {d[1]}')
    
if __name__ == '__main__':
    main()