import sys
from collections import Counter

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

    # with open('/Users/romanroman/projects/algo_trainning/code_run_2/449.Combo/1.txt', 'r') as f:
    #     rows = f.readlines()

    
    goods = list(map(int, rows[1].split()))
    combo_price = int(rows[2])
    combo = list(map(int, rows[3].split()))
    purchase = list(map(int, rows[5].split()))
    combo = set(combo)
    # print('goods :', goods)
    # print('combo :', combo)
    # print('combo_price :', combo_price)
    # print('purchase :', purchase)

    purchase = Counter(purchase)
    # print(purchase)

    total_prise = 0
   
    while sum(purchase.values()) > 0:
      
        # print('before: ')
        # print(purchase)

        _in_combo = []
        _not_in_combo = []
        for c in combo:
            if c in purchase and purchase[c] > 0:
                _in_combo.append(c)
            
            if c not in purchase and purchase[c] > 0:
                _not_in_combo.append()
        
        # print('_in_combo     :', _in_combo)
        # print('_not_in_combo :', _not_in_combo)
        
        if _in_combo:
            _pure_price = 0
            for c in _in_combo:
                _pure_price += goods[c-1]
        
            # print('_pure_price :', _pure_price)

            total_prise += min(_pure_price, combo_price)

            for c in _in_combo:
                purchase[c] -=1
        else:

            _prise = 0
            for ps, num in purchase.items():
                _prise += goods[ps-1] * num
                purchase[ps] -= num
            
            total_prise += _prise



        # print('after: ')
        # print(purchase)
        # break

    print(total_prise)

if __name__ == '__main__':
    main()