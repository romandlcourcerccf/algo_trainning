import sys
from queue import Queue


def mult_array(s_probs):
    res = 0.0
    for p in s_probs:
       res +=p
    return res

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
                                      
    rows = sys.stdin.readlines()

    # with open('/Users/romanroman/projects/algo_trainning/code_run_0/probability_theory/204.Error/1.txt', 'r') as f:
    #     rows = f.readlines()

    
    s_probs = []

    for i in range(1, len(rows)):
        i_prob = list(map(int, rows[i].split()))
        i_prob = [p/100.0 for p in i_prob]
        s_probs.append(i_prob)


    for i in range(len(s_probs)):
        s_probs[i] = s_probs[i][1] *  s_probs[i][0] 


    res = []
    norm_coeff = mult_array(s_probs)

    for i in range(len(s_probs)):
        res.append(s_probs[i]/norm_coeff)

    for r in res:
        print(r)

if __name__ == '__main__':
    main()