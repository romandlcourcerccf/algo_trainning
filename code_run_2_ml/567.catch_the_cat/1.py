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

    visited = set()

    def get_neighbors(border_point, arr, counter):

        visited.add(border_point)
        arr[border_point[0]][border_point[1]] = counter

        neigbours = []
        cols, rows = len(arr), len(arr[0])
        x,y =  border_point[0], border_point[1]

        if x-1 >= 0 and arr[x-1][y] == 1 and (x-1, y) not in visited:
            neigbours.append((x-1, y))

        if x+1 < cols and arr[x+1][y] == 1 and (x+1, y) not in visited:
            neigbours.append((x+1, y))
        
        if y+1 < rows and arr[x][y+1] == 1 and (x, y+1) not in visited:
            neigbours.append((x, y+1))

        if y-1 >= 0 and arr[x][y-1] == 1 and (x, y-1) not in visited:
            neigbours.append((x, y-1))

        return neigbours
        
        
    def bfs(start, arr, counter):
        border = Queue()
        border.put(start)
       
        while not border.empty():
            border_point = border.get()
            neighbors = get_neighbors(border_point, arr, counter)
            
            for neigbour in neighbors:
                border.put(neigbour)

            
    arr = []

    with open('/Users/romanroman/projects/algo_trainning/code_run_2_ml/567.catch_the_cat/4.txt', 'r') as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]

    # rows = sys.stdin.readlines()


    for r in rows:
        arr.append(list(map(int, r.split())))

    rows = len(arr)
    cols = len(arr[0])

    counter = 1
    for row in range(rows):
        for col in range(cols):
            if arr[row][col] == 1 and (row, col) not in visited:
                bfs((row, col), arr,  counter)
                counter +=1

    print(counter-1)
    for r in arr:
        print(" ".join(list(map(str, r))))
    

if __name__ == '__main__':
    main()