import sys
import os

def main():

    import os
    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, '1.txt')
    with open(filename, 'r') as f:
        nums = f.readline()

    print(nums)
    
    # rows = sys.stdin.readlines() 
    # nums = rows[1]
    # nums = list(map(int, nums.split()))
    # pref_summ = [0]*(len(nums)+1)

    # for i in range(1,len(pref_summ)):
    #     pref_summ[i] = pref_summ[i-1] + nums[i-1]

    # pref_summ = list(map(str, pref_summ))

    # print(' '.join(pref_summ[1:]))

    

if __name__ == '__main__':
    main()

