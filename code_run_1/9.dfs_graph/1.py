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

    rows.append('4 5')
    rows.append('2 2')
    rows.append('3 4')
    rows.append('2 3')
    rows.append('1 3')
    rows.append('2 4')
    g = {} 
    
    
    for r in rows:
       
        if len(r) == 1:
            continue
        r = r.split()
        r = [int(i) for i in r]

       
        
        if r[0] not in g:
            g[r[0]] = []
             
        g[r[0]].append(r[1])

        if r[1] not in g:
            g[r[1]] = []

        g[r[1]].append(r[0])

    res = set()

    def dfs(root):
        print('root :',root)
      
        res.add(root)
        if root in g:
            for c in g[root]:
                if c not in res:
                    dfs(c)
        
    dfs(1)
    
    res = sorted(list(res))
    res = [str(i) for i in res]
    print(len(res))
    print(' '.join(res))
        


if __name__ == '__main__':
    main()