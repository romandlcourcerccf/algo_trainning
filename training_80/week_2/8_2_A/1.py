import os

def main():

    dname = os.path.dirname(__file__)

    filename = os.path.join(dname, "input.txt")
    filename = os.path.join(dname, "1.txt")


    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]

    r_num = int(rows[0])
    rows = [list(r) for r in rows[1:]]
    print(rows)

    dp = [[0 for _ in range(3)] for r in range(r_num)]

    # Add eraly stop case. 

    for r in range(r_num):
        for c in range(3):
            if rows[r][c] != 'W':
                
    

        
        

if __name__ == "__main__":
    main()

   


