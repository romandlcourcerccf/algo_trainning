import os

def main():

    dname = os.path.dirname(__file__)

    filename = os.path.join(dname, "input.txt")
    # filename = os.path.join(dname, "1.txt")
   
    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]


    rows = [list(map(int, row.split(' '))) for row in rows[1:]]

    xs = [row[0] for row in rows]
    ys = [row[1] for row in rows]

    xs.sort()
    ys.sort()

    x_min, x_max =  xs[0], xs[-1]
    y_min, y_max =  ys[0], ys[-1]

    print(f'{x_min} {y_min} {x_max} {y_max}' )
    
if __name__ == '__main__':
    main()