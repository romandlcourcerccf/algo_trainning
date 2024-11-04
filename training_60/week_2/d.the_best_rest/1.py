import sys
import os

def main():

    # rows = sys.stdin.readlines()

    import os
    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, '1.txt')
   
    with open(filename, 'r') as f:
        rows = f.readlines()

    _,dist = map(int,rows[0].split())
    print(dist)
    nums = list(map(int,rows[1].split()))
    print(nums)
    nums.sort()

    result = []

    cur_part = []
    l, r = 0, len(nums)
    while l <= r:
        if abs(nums[l]-nums[r]) > dist:
            
            

    
    # 4 2 1


    print(len(result))

if __name__ == '__main__':
    main()

