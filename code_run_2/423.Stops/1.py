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

    with open('/Users/romanroman/projects/algo_trainning/code_run_2/423.Stops/1.txt', 'r') as f:
        rows = f.readlines()

    stops = list(map(int, rows[1].split()))
    requests = list(map(int, rows[2].split()))

    res = []

    requests.sort()

    cur_req = requests.pop(0)
    for i_s, s in enumerate(stops):
        if not requests:
            break

        if stops[i_s] == cur_req:
            res.append(stops[i_s])

        elif stops[i_s] > cur_req:
            
            if i_s-1 >=0:
                res.append(stops[i_s-1])
            else:
                res.append(stops[i_s])

        cur_req = requests.pop(0)

    # while cur_stop_index <= len(stops)-1 and requests:

    #     while stops[cur_stop_index] <= cur_req and cur_stop_index <= len(stops)-1:
        
    #         if stops[cur_stop_index] == cur_req:
    #             res.append(stops[cur_stop_index])
    #             break
    #         cur_stop_index +=1
        
    #     print('stops[cur_stop_index] :', stops[cur_stop_index] , 'cur_req :',  cur_req)
    #     if stops[cur_stop_index] > cur_req:
    #         print('stops[cur_stop_index] :', stops[cur_stop_index])
    #         print('cur_req               :', cur_req)
    #         if cur_stop_index < len(stops)-1:
    #             if cur_stop_index-1 > 0:
    #                 res.append(stops[cur_stop_index-1])
    #             else:
    #                 res.append(stops[cur_stop_index])
    #         else:
    #             res.append(stops[cur_stop_index-1])

    #     cur_req = requests.pop(0)
    #     # cur_stop_index +=1

    print(res)


   
        
if __name__ == '__main__':
    main()