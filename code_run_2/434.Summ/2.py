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
    rows = sys.stdin.readlines()

    # with open('/Users/roman/projects/algo_trainning/code_run_2/434.Summ/1.txt', 'r') as f:
    #     rows = f.readlines()

    #     for i in range(len(rows)):
    #         rows[i] = rows[i].rstrip()

    target = int(rows[0])
        
    res = set()

    def dfs(i, tmp):

        if i <= 0:
            return
            
        tmp.append(i)
            
        if sum(tmp) == target:

            res.add(tuple(sorted(tmp.copy(), reverse=True)))
            return
            
        if sum(tmp) > target:
            return
              
            
        dfs(i, tmp.copy())
        dfs(i+1, tmp.copy())
           
    
    for j in range(target, 0, -1):
        for i in range(1, target):
            dfs(i, [j])
        
    res_str = []
    for r in res:
        r = list(map(str, r))
        res_str.append(' + '.join(r))
        
    res_str.sort()
    res_str.append(str(target))

    for r in res_str:
        print(r)

        
if __name__ == '__main__':
    main()