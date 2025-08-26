import os

def get_min(arr: list[int]) -> int:

    min1 = min2 = float('inf')

    for n in arr:
        if n <= min1:
            min2 = min1
            min1 = n
        elif min1 <= n <= min2:
            min2 = n

    return min1, min2


def get_max(arr: list[int]) -> int:
    max1 = max2 = float('-inf')

    for n in arr:
        if n >= max1:
            max2 = max1
            max1 = n
        elif max1 >= n >= max2:
            max2 = n

    return max2, max1


def main():

    dir_name = os.path.dirname(__file__)
    # filename = os.path.join(dir_name, "input.txt")
    filename = os.path.join(dir_name, "2.txt") 
  
    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    row = rows[0]
    row = [int(n) for n in row.split()]

    print('row :', sorted(row))
   
    min1, min2 = get_min(row)
    max2, max1 = get_max(row)

    print(f'min1 {min1}, min2 {min2} ')
    print(f'max1 {max2}, max2 {max1} ')

    if max2 * max1 >  min1 * min2:
        print(*[max2, max1])
    else:
        print(*[min1, min2])

    
if __name__ == '__main__':
    main()