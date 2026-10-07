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
    # servers_info = sys.stdin.readlines()

    # servers_info = []
    # servers_info.append('2')
    # servers_info.append('50 1')
    # servers_info.append('50 2')

    # print('servers_info :',servers_info)

    servers_info = []
    servers_info.append("3")
    servers_info.append("10 100")
    servers_info.append("30 10")
    servers_info.append("60 2")

    probs = []
    for s_i in range(1, len(servers_info)):
        server_info = servers_info[s_i].split()
        server_info = [float(i) for i in server_info]
        probs.append(
            (
                server_info[0] / 100.0,
                (server_info[0] / 100.0) * (server_info[1] / 100.0),
            )
        )

    res = []
    for i in range(len(probs)):
        si = probs[i][0] * probs[i][1]
        ss = 0
        for j in range(len(probs)):
            print(">> j", j)
            ss += probs[j][0] * probs[j][1]

        res.append(si / ss)

    for r in res:
        print(r)


if __name__ == "__main__":
    main()
