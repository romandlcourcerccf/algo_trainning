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
    rows.append('2')
    rows.append('Alice')
    rows.append('Bob')
    rows.append('5')
    rows.append('1:0 Alice')
    rows.append('1:1 Bob')
    rows.append('2:1 Alice')
    rows.append('4:1 Alice')
    rows.append('4:5 Bob')

    rows = []
    rows.append('2')
    rows.append('Alice')
    rows.append('Bobby')
    rows.append('1')
    rows.append('0:2 Bobby')

    # rows = sys.stdin.readlines() 

    gamers_count = int(rows[0])
    gamers = rows[1:gamers_count+1]
    # print(gamers)

    games_count = int(rows[gamers_count+1])
    # print(games_count)

    games = rows[gamers_count+2:]
    # print(games)

    h = defaultdict(int)

    for gamer in gamers:
        h[gamer]=0
    
    count_stack = []
    for i,g in enumerate(games):
        
        _g = g.split()
        count, gamer = _g[0], _g[1]
        count = count.split(':')
        count = [int(c) for c in count]

        # print('len(count) :',len(count))
        # print('gamer :', gamer)

    
        if i == 0:
            h[gamer] += max(count[0], count[1])
        else:
            prev_count = count_stack[-1]

            cur_count = 0
            if prev_count[0] < count[0]:
                cur_count = count[0] - prev_count[0]
            
            if prev_count[1] < count[1]:
                cur_count = count[1] - prev_count[1]

            h[gamer] += cur_count
        
        count_stack.append((count[0], count[1]))

        # print(f'count {count} gamer {gamer}')

    max_contribute = float('-inf')
    max_contributor = None

    for k,v in h.items():
        if v > max_contribute:
            max_contribute = v
            max_contributor = k

    print(f'{max_contributor} {max_contribute}')


if __name__ == '__main__':
    main()