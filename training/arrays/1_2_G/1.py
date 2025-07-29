import os

def main():

    dir_name = os.path.dirname(__file__)
    # filename = os.path.join(dir_name, "input.txt")
    filename = os.path.join(dir_name, "5.txt") 
  
    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    row = rows[0]
    row = [int(n) for n in row.split()]

    print('row :', row)
    
    if row[0] >= row[1]:
        max1 = row[0]
        max2 = row[1]

        min1 = row[1]
        min2 = row[0]

    else:
        max2 = row[1]
        max1 = row[0]

        min1 = row[0]
        min2 = row[1]

    # print('max1 :', max1, 'max2 :', max2)
    # print('min1 :', min1, 'min2 :', min2)


    for i in range(2, len(row)):
    
        if row[i] >= max1:
            max2, max1  = max1, row[i]
        elif  row[i] >= max2 and row[i] <= max1:
            max2 =  row[i]

        if row[i] <= min1:
            min2 = min1
            min1  = row[i]
           
        elif  min1<=row[i] <= min2:
            min2 = row[i]


    print('max1 :', max1, 'max2 :', max2)
    print('min1 :', min1, 'min2 :', min2)

    if max1 * max2 >= 0 and min1 * min2 >= 0:
        if max1 * max2 >= min1 * min2:
            print(*[max1, max2])
        else:
            print(*[min1, min2])
    


if __name__ == '__main__':
    main()