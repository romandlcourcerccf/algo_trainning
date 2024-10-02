import sys
from queue import Queue

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

    with open('/Users/romanroman/projects/algo_trainning/code_run_0/dfs/11.Cycle/4.txt', 'r') as f:
        rows = f.readlines()

    adj_matrix = []

    for i in range(1, len(rows)):
        adj_matrix.append(list(map(int, rows[i].split())))
    
    vertices = set(list(range(len(adj_matrix))))
    # print(vertices)
    visited = set()
    cycle_path = []

    def dfs(root, adj_matrix, path, cycle_path):
    
        if root in path:
            cycle_path.append(path) 
            return

        path.append(root)
        visited.add(root)

        children = {i for i in range(len(adj_matrix[root])) if i not in visited and  adj_matrix[root][i] != 0}

        if not children:
            return
        
        for chind in children:
            dfs(chind, adj_matrix, path, cycle_path)

    while vertices:
        
        cur = next(iter(vertices))
        # print('start :', cur)

        path = []
        dfs(cur, adj_matrix, path, cycle_path)
        # print(path)

        vertices = vertices - set(path)
    
   
    # print('>>' ,cycle_path)

    if not(cycle_path):
        print('NO')
    else:
        print('YES')
        print(len(cycle_path[0]))
        path = [str(i+1) for i in cycle_path[0]]
        print(' '.join(path))


    

if __name__ == '__main__':
    main()