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

    with open('/Users/roman/projects/algo_trainning-1/ya_prep/code_run/binary_search/ 77.Emprove_grades/1.txt', 'r') as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]
  
    rows = list(map(int, rows))
    a, b, c = rows[0], rows[1], rows[2]
    e = a+b+c 

    av_score = (2*a+3*b+4*c+5*e)/(a+b+c+e)
    
    while sum < 4
        av_score = av_score/2
        av_score = (2*a+3*b+4*c+5*e)/(a+b+c+e)

    print(sum)

if __name__ == '__main__':
    main()