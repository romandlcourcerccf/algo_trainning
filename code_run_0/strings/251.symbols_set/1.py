import sys


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

    with open('/Users/romanroman/projects/algo_trainning/code_run_0/strings/251.symbols_set/7.txt', 'r') as f:
        rows = f.readlines()
       
    rows = [r.strip() for r in rows]

    s = rows[0]
    c = set(rows[1])

    if len(c) == 0 or len(s) == 0:
        print('0')
        return
    
    if len(c) > len(s):
        print('0')
        return

    min_len = float('inf')

    _c = set()
    _min_len = 0

    pos = 0
    while pos <= len(s)-1:

        if s[pos] in c:

            _min_len +=1
            _c.add(s[pos])

            if _c == c:
                min_len = min(min_len, _min_len)

        else:
            _min_len = 0
            _c = set()
       
        pos +=1
    
    print(min_len if min_len != float('inf') else '0') 


if __name__ == '__main__':
    main()
