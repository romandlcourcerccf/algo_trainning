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
    # rows.append('2')
    # rows.append('aaaaaaaaaaaaa')
    # rows.append('aaabbbaaabbba')

    # rows.append('2')
    # rows.append('abab')
    # rows.append('baba')

    rows.append('1')
    rows.append('qwertyqwertyqwertyqwertyqwerty')
   
    vertices = defaultdict(set)
    nodes =    defaultdict(int)

    for i, row in enumerate(rows):
        if i == 0:
            continue

        print(f'row : {row}')
        for i in range(0, len(row)-3):
            in_vert, out_vert = row[i:i+3], row[i+1:i+4]
            vertices[in_vert].add(out_vert)
            nodes[in_vert+out_vert] +=1


    print(len(vertices))       
    print(len(nodes))

    for k,v in nodes.items():
        print(f'{k[0:3]} {k[3:]} {v}')


if __name__ == '__main__':
    main()