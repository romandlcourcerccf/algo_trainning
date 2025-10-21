import os
from collections import defaultdict


def main():
    dname = os.path.dirname(__file__)

    filename = os.path.join(dname, "input.txt")
    filename = os.path.join(dname, "1.txt")
    # filename = os.path.join(dname, "2.txt")
    # filename = os.path.join(dname, "3.txt")
    # filename = os.path.join(dname, "4.txt")
    # filename = os.path.join(dname, "5.txt")


    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]

    nums = list(map(int, rows[1].split()))

    def is_symmetric(seq):
        l, r = 0, len(seq)-1
        while l < r:
            if seq[l] != seq[r]:
                return False
            l +=1
            r -=1
        return True
    
    for pos in range(len(nums)):
        if is_symmetric(nums + nums[0:pos][::-1]):
            print(len(nums[0:pos][::-1]))
            print(*nums[0:pos][::-1])
            return

    



        



if __name__ == "__main__":
    main()
