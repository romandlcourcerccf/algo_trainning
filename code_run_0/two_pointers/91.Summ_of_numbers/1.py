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

    with open('/Users/romanroman/projects/algo_trainning/code_run_0/two_pointers/91.Summ_of_numbers/4.txt', 'r') as f:
        rows = f.readlines()

    hit_counter = 0
    numbers = list(map(int, rows[0].split()))
    N,K = numbers[0], numbers[1]

    numbers = list(map(int, rows[1].split()))
    
    l, r = 0, 0
    while l <= len(numbers)-1 and r <= len(numbers)-1:
    
        if l<len(numbers)-1 and r < len(numbers)-1:
            if sum(numbers[l:r+1]) < K:
                r+=1
            elif sum(numbers[l:r+1]) > K:
                l+=1
            else:
                hit_counter +=1
                r+=1
        elif r == len(numbers)-1:
            if sum(numbers[l:r+1]) == K:
                hit_counter +=1
            l +=1
           

    print(hit_counter)
        

if __name__ == '__main__':
    main()
