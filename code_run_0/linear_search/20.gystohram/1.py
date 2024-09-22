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
                                      
    # rows = sys.stdin.readlines()

    with open('/Users/romanroman/projects/algo_trainning/code_run_0/linear_search/20.gystohram/7.txt', 'r') as f:
        rows = f.readlines()

    numbers = list(map(int, rows[0].split()))
    
    i = numbers[0]
    is_same = True
    for i in  range(1, len(numbers)):
        if numbers[i-1] != numbers[i]:
            is_same = False
            break

    if is_same:
        print(numbers[0] * len(numbers))
        return

    i = numbers[0]
    is_esc = True
    for i in  range(1, len(numbers)):
        if numbers[i-1] > numbers[i]:
            is_esc = False
            break

    if is_esc:
        max_square  = float('-inf')

        for i in range(len(numbers)):
            _max_square = numbers[i] * (len(numbers)-i)
            max_square = max(max_square, _max_square)
        print(max_square)
        return

    
    max_square  = float('-inf')
    st = []

    for i in range(len(numbers)):
        if not st or numbers[st[-1]] < numbers[i]:
           st.append(i)
        else:
             while st and numbers[st[-1]] > numbers[i]:
                 _i = st.pop()
                 _max_square = (i - _i) * max(numbers[i], numbers[_i]) 
                 max_square  = max(_max_square, max_square)
                 
            
    print(max_square)
    

if __name__ == '__main__':
    main()