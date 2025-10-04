import os
import itertools
import numpy as np

def main():

    dname = os.path.dirname(__file__)

    filename = os.path.join(dname, "input.txt")
    filename = os.path.join(dname, "1.txt")
    # filename = os.path.join(dname, "2.txt")
    filename = os.path.join(dname, "3.txt")
   

    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]

    arr = []   
    for r in rows[1:]:
        arr.append(list(r))

    for r in arr:
        print(r)

    for r in arr:
        
        print(r)
        
        pos = 0
        cur_smb = r[pos]
        max_ln = float('-inf')
        max_ln_smb = ''
        ln = 1

        while pos < len(r)-1:
            pos +=1
            if r[pos] == cur_smb:
                ln +=1
            else:
                if ln >= max_ln:
                    max_ln = ln
                    max_ln_smb = cur_smb

                ln = 1
                cur_smb = r[pos]

        if ln >= max_ln:
            max_ln = ln
            max_ln_smb = cur_smb

        print(max_ln)
        print(max_ln_smb)


       

        
    



        
    


    # for r in rows[1:]:
    #     arr.append(list(r))
    
    # for r in arr:
    #     print(r)

    



if __name__ == "__main__":
    main()

