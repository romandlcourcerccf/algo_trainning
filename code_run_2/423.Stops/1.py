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

    rows = []

    rows.append('3 2')
    rows.append('1 3 5')
    rows.append('4 1')

    stops = rows[1].split()
    stops = list(map(int, stops))
    
    buses = rows[2].split()
    buses = list(map(int, buses))

    stops.sort()
    buses.sort()

    res = []

    for i, stop in enumerate(stops):

        if not buses:
            break
        
        cur_bus = buses[0]
            
        if stop == cur_bus:
           
            res.append(stop)
            buses.pop(0)
        elif stop > cur_bus:
            if stops[i-1] > 0:
                res.append(i)
            else:
                res.append(i+1)

            buses.pop(0)
    
    if len(buses) > 0:
        for bus in buses:
            res.append(len(stops))

    for r in res:
        print(r)
    
    


if __name__ == '__main__':
    main()