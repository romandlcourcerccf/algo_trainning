import os

from collections import Counter

def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    # filename = os.path.join(dir_name, "1.txt")
    # filename = os.path.join(dir_name, "2.txt")
    # filename = os.path.join(dir_name, "3.txt")
    # filename = os.path.join(dir_name, "7.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    # print(rows)
    # print(tuple(map(int, rows[0].split())))
    n, k = tuple(map(int, rows[0].split()))
    nums = list(map(int, rows[1].split()))

    h = {}
    for i in range(len(nums)):
        if nums[i] in h and abs(i - h[nums[i]]) <= k:
            print('YES')
            return
        
        h[nums[i]] = i

    print('NO')


if __name__ == '__main__':
    main()