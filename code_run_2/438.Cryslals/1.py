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
    
    rows = []
    rows.append('aaaza')
    rows.append('aazzaa')
    rows.append('azzza')

    # rows = []
    # rows.append('xy')
    # rows.append('xxyy')
    # rows.append('yx')

    def get_min(a, b, c):
        if a == b:
            return 2, a
        elif a == c:
            return 1, a
        else:
            return 0, b
        
    def collapse(str, idx):
        return str[0:idx]+str[idx+1:]

    def double(str, idx):
        return str[0:idx]+str[idx]+str[idx:]
        
    for i in range(0, min(len(rows[0]), len(rows[1]), len(rows[2]))):
        if rows[0][i] == rows[1][i] == rows[2][i]:
            continue

        if i == len(rows[0])-1 or i == len(rows[1])-1 or i == len(rows[2])-1:
            break
        
        min_index, max_smbl = get_min(rows[0], rows[1], rows[2])


        if i>0 and i<len(rows[min_index])-1  and \
              rows[min_index][i-1] == rows[min_index][i] and \
                  rows[min_index][i+1] == max_smbl:
              
              collapse(rows[min_index], i)


        

if __name__ == '__main__':
    main()