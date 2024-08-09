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
    nums = sys.stdin.readlines()[0].split()
    # nums = [1,2,1,2,2]
    nums = [int(n) for n in nums]

    def is_symmetric(l, r):
        while l < r:
            if nums[l] != nums[r]:
                return False

            l+=1
            r-=1

        return True
        
    pos = 0
    while pos <= len(nums)-1:
        if nums[pos] == nums[-1]:
            if is_symmetric(pos, len(nums)-1):
                break
        pos +=1

    nums = nums[0:pos][::-1]
    nums = [str(n) for n in nums]

    print(len(nums))
    print(' '.join(nums))

if __name__ == '__main__':
    main()