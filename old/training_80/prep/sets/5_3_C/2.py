import os

from collections import defaultdict

def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    # filename = os.path.join(dir_name, "1.txt")
    # filename = os.path.join(dir_name, "2.txt")
    filename = os.path.join(dir_name, "7.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    nums = list(map(int, rows[1].split()))

    # print(nums)

    nums.sort()

    # print(nums)


    r = len(nums)-1
    
    removed = []

    while abs(nums[0]-nums[r]) > 1 and r >= 0:
        removed.append(nums[r])
        r -=1

    print(len(removed))



    
        
    

if __name__ == '__main__':
    main()