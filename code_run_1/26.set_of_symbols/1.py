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
    # s1 = rows[0]
    # s2 = rows[1]

    # s1 = 'abba'
    # s2 = 'ab'

    s1 = "accbdd"
    s2 = "ca"

    need = [0] * 26
    have = [0] * 26

    for c in s2:
        print(ord(c))
        have[ord(c) - 97] += 1

    res, len_res = [-1, -1], float("inf")
    l = 0
    for r in range(len(s1)):
        c = s1[r]
        need[ord(c) - 97] += 1

        all_exeed = True
        for i in range(len(need)):
            if need[i] > 0 and have[i] < need[i]:
                all_exeed = False
                break
        if all_exeed:
            if (r - l + 1) < len_res:
                res = [l, r]
                len_res = r - l + 1

            while all_exeed:
                l += 1

                if need[ord(s1[l]) - 97] > 0:
                    have[ord(l) - 97] -= 1

                    for i in range(len(need)):
                        if need[i] > 0 and have[i] < need[i]:
                            all_exeed = False
                            break

    print(res)


if __name__ == "__main__":
    main()
