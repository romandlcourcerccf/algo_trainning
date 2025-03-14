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
    # rows = sys.stdin.readlines()
    # row = rows[0]

    row = "ABCABC A"
    # row = 'AB A'
    # row = ' ABCABC A AB AB C A'
    # row = ' A BC AB     C A A   B A BC A'
    # row = '     A BC AB     C A A   B A BC A AAAAAAAAAAA    '
    words = row.split(" ")
    pairs = defaultdict(int)

    for w in words:
        if len(w) >= 2:
            pos = 0
            while pos < len(w) - 1:
                pairs[w[pos : pos + 2]] += 1
                pos += 1

    sorted_pairs = dict(sorted(pairs.items(), key=lambda x: (-x[1], -ord(x[0][0]))))

    print(next(iter(sorted_pairs)))


if __name__ == "__main__":
    main()
