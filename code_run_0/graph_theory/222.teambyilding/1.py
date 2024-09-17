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

    with open('/Users/romanroman/projects/algo_trainning/code_run_0/graph_theory/222.teambyilding/1.txt', 'r') as f:
        rows = f.readlines()

    
    graph_info = rows[0]
    graph_info = list(map(int, graph_info.split()))

    vert_count, edges_count = graph_info[0], graph_info[1]

    graph_edges = {}


    for i in range(1, len(rows)):
        edge_info = list(map(int, rows[i].split()))
        graph_edges[i] = edge_info[1]


    for i in range(edges_count):

        used_edges = set()
        for edge in graph_edges:
            current_edge = edge
            if current_edge in graph_edges.keys() and current_edge not in used_edges:
                current_edge = graph_edges[current_edge]
            break

        print(used_edges)

if __name__ == '__main__':
    main()