import sys
from collections import defaultdict
from typing import List
def naive_check(row: int, col: int, square: List[str]) -> bool:
    hits = 0
    symbols = ['X', 'O']

    rows = len(square)
    cols = len(square[0])

    if not (col+5 <= cols or row+5 <= rows):
        return 
    
    for s in symbols:
        
        if col+5 <= cols:
            for c in range(col, col+5):
                is_full = True
                for r in range(row, row+5):
                    if square[r][c] != s:
                        is_full = False
                if is_full:
                    hits +=1

        if row+5 <= rows:
            for r in range(row, row+5):
                is_full = True
                for c in range(col, col+5):
                    if square[r][c] != s:
                        is_full = False
                if is_full:
                    hits +=1

        if col+5 <= cols and row+5 <= rows:
            is_full = True
            for i in range(0, 5):
                if square[row+i][col+i] != s:
                    is_full = False
            if is_full:
                    hits +=1

            is_full = True
            for i in range(0, 5):
                if square[row+i][col+4-i] != s:
                    is_full = False
        
            if is_full:
                hits +=1

    return hits > 0


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

    with open('/Users/romanroman/projects/algo_trainning/code_run_2/444.tic_tac_toe/2.txt', 'r') as f:
        rows = f.readlines()

    print(rows)

    dim = list(map(int, rows[0].split()))
    
    square = []

    for i in range(1, len(rows)):
        square.append(rows[i])

    for i in range(len(square)):
        print('>>',rows[i])
    
   
if __name__ == '__main__':

    test_square = []
    # test_square.append('XXXXX.')
    # test_square.append('......')
    # test_square.append('X.O...')
    # test_square.append('X.O...')
    # test_square.append('X.O...')
    # test_square.append('X.O...')
    # test_square.append('..O...')


    # test_square.append('XXXXX.')
    # test_square.append('X.....')
    # test_square.append('.X....')
    # test_square.append('..X...')
    # test_square.append('...X..')
    # test_square.append('....X.')


    test_square.append('XXXXX.')
    test_square.append('X....O')
    test_square.append('.X..O.')
    # test_square.append('...O..')
    # test_square.append('..O...')
    # test_square.append('.O..X.')

    print('rows :', len(test_square))
    print('cols :', len(test_square[0]))

    print(naive_check(0,0, test_square))
    # print(naive_check(1,1, test_square))
    # print(naive_check(1,1, test_square))

    # main()