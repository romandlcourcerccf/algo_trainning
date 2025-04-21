def find_max_route(n, m, matrix):
    # Создаем таблицу для хранения максимальных сумм
    dp = [[0] * m for _ in range(n)]
    # Создаем таблицу для хранения маршрутов
    path = [[''] * m for _ in range(n)]

    dp[0][0] = matrix[0][0]  # Начальная клетка

    # Заполняем первую строку
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + matrix[0][j]
        path[0][j] = path[0][j-1] + 'R'

    # Заполняем первый столбец
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + matrix[i][0]
        path[i][0] = path[i-1][0] + 'D'

    for p in path:
        print(p)

    # Заполняем оставшиеся клетки
    for i in range(1, n):
        for j in range(1, m):
            if dp[i-1][j] > dp[i][j-1]:
                dp[i][j] = dp[i-1][j] + matrix[i][j]
                path[i][j] = path[i-1][j] + 'D'
            else:
                dp[i][j] = dp[i][j-1] + matrix[i][j]
                path[i][j] = path[i][j-1] + 'R'

    return dp[n-1][m-1], path[n-1][m-1]


import os
dname = os.path.dirname(__file__)

filename = os.path.join(dname, "1.txt")

with open(filename, "r") as f:
    lines = f.readlines()

dp = []
matrix = []

dim = lines[0].split()
n, m = int(dim[0]), int(dim[1])

for row in lines[1:]:
    matrix.append(list(map(int, row.split())))

# Находим максимальную сумму и путь
max_sum, route = find_max_route(n, m, matrix)

# Выводим результаты
print(max_sum)
print(' '.join(route))