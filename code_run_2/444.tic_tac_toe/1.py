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
    rows = []
    rows.append('5 6')
    rows.append('XX...O')
    rows.append('XXXXXO')
    rows.append('.....O')
    rows.append('.....O')
    rows.append('.....O')


    rows = []
    rows.append('5 6')
    rows.append('X.....')
    rows.append('OXOOOO')
    rows.append('OOXOOO')
    rows.append('OOOXOO')
    rows.append('OOOOXO')

    dim = list(map(int, rows[0].split()))
   

    arr = []
    for r in range(1, len(rows)):
        print(r)
        arr.append(list(rows[r]))

    res = {}
    res['X'] = 0
    res['O'] = 0

    def check_square(col, row, arr, res):

        print('\n')
        for r in range(row, row+5):
            print('r :',r)
            start_smbl = arr[r][col] 
            if start_smbl not in ['X', 'O']:
                continue

            is_win = True
            for c in range(col, col+5):
                if arr[r][c] != start_smbl:
                    is_win = False
                    break
            if is_win:
                res[start_smbl] += 1


        for c in range(col, col+5):
            if arr[0][c] not in ['X', 'O']:
                continue

            start_smbl = arr[row][c] 
            is_win = True
            for r in range(row, row+5):
                if arr[r][c] != start_smbl:
                    is_win = False
                    break
            if is_win:
                res[start_smbl] += 1

        start_smbl =  arr[row][col]
        if start_smbl in ['X', 'O']:
            is_win = True
            for i in range(5):
                if arr[row+i][col+i] != start_smbl:
                    is_win = False
            if is_win:
                res[start_smbl] += 1
        

        start_smbl =  arr[row][col+4]
        if start_smbl in ['X', 'O']:
            is_win = True
            for i in range(5):
                if arr[row+i][col-i] != start_smbl:
                    is_win = False
            if is_win:
                res[start_smbl] += 1

    rows = dim[0]
    cols = dim[1]
    print(f'rows {rows} cols {cols}')

    for row in arr:
        print(row)


    print(arr[0][3])

    for row in range(0, rows-4):
        for col in range(0, cols-4):
            print('row :', row, 'col :', col)
            check_square(col, row, arr, res)

    print(res)
   
if __name__ == '__main__':
    main()