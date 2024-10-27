import sys


def main():
   

    # rows = sys.stdin.readlines()

    import os
    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, '2.txt')
    
    with open(filename, 'r') as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]

   
    x1, y1, x2, y2, x, y = int(rows[0]), int(rows[1]), int(rows[2]), int(rows[3]), int(rows[4]), int(rows[5])

    print(f'x1 : {x1}, y1 : {y1}, x2 : {x2}, y2 : {y2}, x : {x}, y : {y}')

    res = ''

    if x <= x1 and y >= y2:
        res = 'NW'
    elif x <= x1 and y <= y1:
        res = 'SW'
    elif x >= x2 and y <= y1:
        res = 'SE'
    elif x >= x2 and y >= y2:
        res = 'NE' 
    elif x <= x1 and y1<y<y2:
        res = 'W'
    elif y <= y1 and x1<x<x2:
        res = 'S'
    elif x >= x2 and y1<y<y2:
        res = 'E'
    elif y >= y2 and x1<x<x2:
        res = 'N'  

    print(res)
   
if __name__ == '__main__':
    main()
