import sys


def bin_search(arr, target):
    l, r = 0, len(arr)
    while l <= r:
        m = (l + r) // 2

        if m == 0 and arr[m] != target:
            return {"type": "left_most", "val": arr[0], "index": 0}
        elif m > len(arr) - 1:
            return {"type": "right_most", "val": arr[-1], "index": len(arr) - 1}

        if arr[m] == target:
            return {"type": "target", "val": arr[m], "index": m}
        elif arr[m] < target:
            l = m + 1
        else:
            r = m - 1

    return {"type": "middle", "val": arr[r], "index": r}


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

    with open(
        "/Users/romanroman/projects/algo_trainning/code_run_2/423.Stops/1.txt", "r"
    ) as f:
        rows = f.readlines()

    stops = list(map(int, rows[1].split()))
    requests = list(map(int, rows[2].split()))

    res = []
    for req in requests:
        _r = bin_search(stops, req)
        match _r["type"]:
            case "target":
                res.append(_r["index"] + 1)

            case "left_most":
                res.append(_r["index"] + 1)
            case "right_most":
                res.append(_r["index"] + 1)
            case "middle":
                res.append(_r["index"] + 1)

    for r in res:
        print(r)


if __name__ == "__main__":
    main()
