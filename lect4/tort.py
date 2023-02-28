def __print(arr):
    for i in range(len(arr)):
        print(arr[i])
    print('\n')

def turtle(field):
    
    rows = len(field)
    cols = len(field[0])

    print('cols :', cols)
    print('rows :', rows)

    dp =  [[0 for r in range(rows+1)] for i in range(cols+1)]
    
    print('dp cols :', len(dp))
    print('dp rows :', len(dp[0]))

    for row in range(1, rows+1):
        for col in range(1,cols+1):
            _col = col-1
            _row = row-1
            dp[row][col] =  max(field[_row-1][_col], field[_row][_col+1]) + field[_row][_col]


    return dp[-1][-1]

field = [[0,1,0,1],[0,2,0,1],[1,1,0,1]]
__print(field)

print(turtle(field))
