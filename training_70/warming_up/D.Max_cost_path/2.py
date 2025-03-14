import sys


# n = int(input())
# a = [2, 4, 7]
# for i in range(3, 36):
#     a.append(a[i - 1] + a[i - 2] + a[i - 3])
# print(a[n - 1])


def main():
    import os
    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, '1.txt')

    with open(filename, 'r') as f:
        rows = f.readlines()

    # rows = int(sys.stdin.readlines())
    
    field = []
    costs = []

    for row in rows[1:]:
        field.append(list(map(int, row.split())))
        costs.append([0]*len(row.split()))



    # for row in range(len(rows)-1):
    #     if row == 0:
    #         costs[row][0] = field[row][0]
    #     else:
    #         costs[row][0] +=  costs[row-1][0] + field[row][0]
    
    # cols = len(rows[1].split())

    # for col in range(cols):
    #     if col == 0:
    #         costs[0][col] = field[0][col]
    #     else:
    #         costs[0][col] +=  costs[0][col-1]+ field[0][col]
    
    # for row in range(1, len(field)):
    #     for col in range(1, len(field[row])):
    #         costs[row][col] = field[row][col] + max(costs[row-1][col], costs[row][col-1])

    
    # row = len(field)-1
    # col = len(field[0])-1

    # path = []
    # while row != 0 and col !=0:
    #     if costs[row][col-1] > costs[row-1][col]:
    #         path.append('R')
    #         col = col-1
    #     else:
    #         path.append('D')
    #         row = row-1
    
    #     print('row :', row, 'col :', col)
    
    # if len(path) < len(field):
    #     if col == 0:
    #         costs += ['D'] * len(field) - len(path) -1
    #     elif row == 0:
    #         costs += ['R'] * len(field) - len(path) -1


    # print(costs[len(field)-1][len(field[0])-1])
    # print(*path)


    row = len(field)-1
    col = len(field[0])-1

    path = []
    sum = field[row][col]

    while row != 0 and col !=0:
        if field[row][col-1] > field[row-1][col]:
            path.append('R')
            col = col-1
            sum += field[row][col-1]
        else:
            path.append('D')
            row = row-1
            sum += field[row-1][col]


    if col == 0 or row == 0 and not (col == 0 or row == 0):

        if col == 0:
           
            path += ['D'] * row 
            for row in range(row, -1, -1):
            
                sum += field[row][col]
        else:
           
            path += ['R'] * col 
            for col in range(col, 0, -1):
                sum += field[row][col]
        
    
    print(sum)
    print(*path)

if __name__ == "__main__":
    main()
