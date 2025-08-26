import os

def get_min(arr: list[int]) -> int:

    min1 = min2 = float('inf')

    for n in arr:
        if n < min1:
            min2 = min1
            min1 = n
        elif min1 < n < min2:
            min2 = n

    return min1, min2


def get_max(arr: list[int]) -> int:
    max1 = max2 = float('-inf')

    for n in arr:
        if n > max1:
            max2 = max1
            max1 = n
        elif max1 > n > max2:
            max2 = n

    return max1, max2


def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    # filename = os.path.join(dir_name, "3.txt") 
  
    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    row = rows[0]
    row = [int(n) for n in row.split()]
    row.sort()

    # print('row :', row)

    if row[-1] * row[-2] > row[0] * row[1]:
        if row[-1] < row[-2]:
            print(*[row[-1], row[-2]])
        else:
            print(*[row[-2], row[-1]])
    else:
        if row[0] < row[1]:
            print(*[row[0], row[1]])
        else:
            print(*[row[1], row[0]])
    
    

if __name__ == '__main__':

    print('>>>')

    arr = [4,-5,5,45]

    print(arr)

    print(get_min(arr))
    print(get_max(arr))

    # main()