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

    rows = sys.stdin.readlines()

    # with open('/Users/romanroman/projects/algo_trainning/code_run_2/441.score_board/1.txt', 'r') as f:
    #     rows = f.readlines()

    #     for i in range(len(rows)):
    #         rows[i] = rows[i].rstrip()

    # print(rows)

    num_players = int(rows[0])
    # print('num_players ', num_players)
    players_scores = defaultdict(int)

    for i in range(1, num_players + 1):
        players_scores[rows[i]] = 0

    # print(players_scores)

    games_num = int(rows[num_players + 1])
    # print(games_num)

    st = []
    for it, round in enumerate(rows[num_players + 2 :]):
        round = round.split()
        scores = list(map(int, round[0].split(":")))
        name = round[1]

        if it == 0:
            score = max(scores)
        else:
            _scores = st.pop()
            if scores[0] > _scores[0]:
                score = scores[0] - _scores[0]
            elif scores[1] > _scores[1]:
                score = scores[1] - _scores[1]

        # print(f'{round} {name} {score}')
        players_scores[name] += score
        st.append(scores)

    max_score = max(players_scores.values())

    res = []
    for k, v in players_scores.items():
        if v == max_score:
            res.append(k)

    res.sort()

    print(f"{res[-1]} {max_score}")


if __name__ == "__main__":
    main()
