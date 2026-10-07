import os

def main():

    dname = os.path.dirname(__file__)

    filename = os.path.join(dname, "input.txt")
    filename = os.path.join(dname, "1.txt")
    # filename = os.path.join(dname, "2.txt")
    # filename = os.path.join(dname, "3.txt")
 

    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]
    
    a, b, S = tuple(map(int, rows[0].split()))

    lw, rw = 0, 1000000

    while lw < rw:
        
        mw =  (lw + rw) // 2
        mh = S // mw

        if abs((mh + b) - (mw + a)) < 0.0001:
            print(mh + b) 
            return

        elif (mh + b) <  (mw + a):
            rw = mw  
        elif (mh + b) >  (mw + a):
            lw = mw +1
    
    print(-1)
        

if __name__ == "__main__":
    main()

   


