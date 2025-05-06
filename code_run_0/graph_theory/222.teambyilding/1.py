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

    with open(
        "/Users/romanroman/projects/algo_trainning/code_run_0/graph_theory/222.teambyilding/2.txt",
        "r",
    ) as f:
        rows = f.readlines()

    graph_info = rows[0]
    graph_info = list(map(int, graph_info.split()))

    vert_count, _ = graph_info[0], graph_info[1]

    graph = defaultdict(set)
    vertices = set([i + 1 for i in range(vert_count)])

    for i in range(1, len(rows)):
        row = rows[i]
        row = list(map(int, row.split()))
        start, end = row[0], row[1]
        graph[start].add(end)
        graph[end].add(start)

    # print(vertices)
    # print(graph)

    res = []

    _vertices = vertices.copy()
    _visited = set()

    for start_vert in vertices:
        if start_vert not in graph.keys():
            continue

        _visited.add(start_vert)

        cur_verts = {start_vert}

        while True:
            _visited = _visited | cur_verts

            cur_verts = cur_verts & graph.keys()

            if not cur_verts:
                break

            neighbours = set()
            for cur_vert in cur_verts:
                if cur_vert in graph.keys():
                    neighbours = neighbours | graph[cur_vert]
                    _visited.add(cur_vert)

            neighbours = neighbours - _visited

            if not neighbours:
                break

            cur_verts = neighbours

        not_visited = _vertices - _visited
        if len(not_visited) > 0:
            res.append([_visited, not_visited])
            break

        _visited = set()

    if res:
        res = res[0]
        print(len(res))
        print(" ".join(map(str, list(res[0]))))
        print(" ".join(map(str, list(res[1]))))
    else:
        print("-1")


if __name__ == "__main__":
    main()
