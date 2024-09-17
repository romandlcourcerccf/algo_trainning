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
                                      
    rows = sys.stdin.readlines()

    # with open('/Users/romanroman/projects/algo_trainning/code_run_0/backend/377.diversity/1.txt', 'r') as f:
    #     rows = f.readlines()

    
    positions = list(map(int, rows[-1].split()))
    positions_map = {}
    categories_map = defaultdict(list)

    for i in range(len(positions)):
       positions_map[positions[i]] = i

    # print(positions_map)

    for i in range(1, len(rows)-1):
        r = list(map(int, rows[i].split()))
        categories_map[r[1]].append(positions_map[r[0]])

    # print(categories_map)

    mininums = []

    lens = []

    for cat, pos in categories_map.items():
        lens.append(len(pos))

    if max(lens) == 1:
        print(len(rows)-2)
        return


    for cat, pos in categories_map.items():
        # print(pos)
        min_diff = float('inf')
        for i in range(0, len(pos)-1):
            min_diff = min(min_diff, pos[1]-pos[0])
        
        # print('cat : ', cat, 'pos : ', pos, 'min : ', min_diff)
        mininums.append(min_diff)

    print(min(mininums))

if __name__ == '__main__':
    main()