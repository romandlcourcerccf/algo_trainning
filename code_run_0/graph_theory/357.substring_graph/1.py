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

    # Если можно, подскажи в какую сторону мыслить в задаче 20.
    # Гистограмма и прямоугольник. 
    # По тегам указано stack и linearSearch,
    # что и пытаюсь реализовать: итерирую по индексам высот столбцов и добавляю в стек 
    # если пустой или высота больше вершины стека, 
    # иначе если меньше,
    # то вычислю площадь и удаляю индексы из стека попутно проверяя пуст ли стек
    # и высота вершины больше текущей.
    # Вроде линейно должно быть.
    # На втором закрытом тесте ловлю w/a и не могу придумать тестовые, 
    # по которым алгоритм не работает((( Буду признателен за совет!
                                      
    # rows = sys.stdin.readlines()

    # _rows = []
    # for r in rows:
    #     _rows.append(r.strip())
    # rows = _rows

    
    with open('/Users/romanroman/projects/algo_trainning/code_run_0/graph_theory/357.substring_graph/3.txt', 'r') as f:
        rows = f.readlines()
        _rows = []
        for r in rows:
            _rows.append(r.strip())
        rows = _rows


    v = defaultdict(int)
    vv = set()
    for row in rows:
        # print('row :', row)
        for i in range(0, len(row)-3):
            start = row[i:i+3]
            end = row[i+1:i+4]

            vv.add(start)
            vv.add(end)

            v[start+end] +=1
            

    
    print(len(vv))
    print(len(v.keys()))

    for k,v in v.items():
        print(f'{k[:3]} {k[3:]} {v}')
    

if __name__ == '__main__':
    main()