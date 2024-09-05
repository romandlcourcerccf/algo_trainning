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

    rows = sys.stdin.readlines()

    # with open('/Users/romanroman/projects/algo_trainning/code_run_0/dict/2.txt', 'r') as f:
    #     rows = f.readlines()

    h = defaultdict(int)

    for row in rows:
        words = row.split()
        for w in words:
            h[w] +=1

    i_h =  defaultdict(list)
    for k,v in  h.items():
        i_h[v].append(k)


    max_count = float('-inf')
    max_words = None

    for k,v in  i_h.items():
        if k >= max_count:
            max_count = k
            max_words = v
        
    max_words.sort()
    print(max_words[0])
    
if __name__ == '__main__':
    main()