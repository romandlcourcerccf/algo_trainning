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

    import os
    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, '1.txt')
   
    with open(filename, 'r') as f:
        rows = f.readlines()

    hit_counter = 0
    numbers = list(map(int, rows[0].split()))
    N,K = numbers[0], numbers[1]

    numbers = list(map(int, rows[1].split()))
    prefix_summs = [0] * (len(numbers)+1)

    for i in range(0, len(numbers)):
        prefix_summs[i+1] = numbers[i] + prefix_summs[i]

    print(numbers)
    print(prefix_summs)


    l, r = 0, 1
    while l <= len(prefix_summs)-1 and r <= len(prefix_summs)-1:
        _sum = prefix_summs[r]-prefix_summs[l]
        if l<len(numbers)-1 and r < len(numbers)-1:
           
            print(_sum)
        
            if _sum < K:
                r+=1
            elif _sum > K:
                l+=1
            else:
                hit_counter +=1
                l+=1
                r+=1
        elif r == len(numbers)-1:
            print('l :', l)
            if _sum == K:
                hit_counter +=1
                
            l+=1
            

    
    print('hit_counter :',hit_counter)
        

if __name__ == '__main__':
    main()
