import sys
import os
from collections import defaultdict, Counter


def get_neighbors(p, field, visited_points):

    rows = len(field)
    cols = len(field[0])

    neighbors = set()

    for x in range(p[0]-1,p[0]+2):
        for y in range(p[1]-1,p[1]+2):
            if (x,y) != p and x>=0 and x < cols and y>=0 and y < rows and field[y][x] != 'X' and (x,y) not in visited_points:
                neighbors.add((x,y))
                visited_points.add((x,y))

    return neighbors 

def calc_rirection(prev_point, cur_point):
    pass

def dfs(point, field, direction, turn_count):

    neighbors = get_neighbors(point, field, )
    pass


def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "1.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    # rows = sys.stdin.readlines()
    # rows = [r.rstrip() for r in rows]

    field = []

    
    for r in rows[1:-2]:
        field.append(list(r))
    
    print(field)

    R, C = tuple(map(int,rows[0].split()))

    print(f'rows {R}, cols {C}')

    start_point = list(map(int, rows[-2].split()))
    end_point = list(map(int, rows[-1].split()))

    print('start_point :',start_point)
    print('end_point :',end_point)

    start_point[0] -= 1
    start_point[1] -= 1

    end_point[0] -= 1
    end_point[1] -= 1

    start_point = tuple(start_point)
    end_point = tuple(end_point)

    print(f'start_point : {start_point}')
    print(f'end_point : {end_point}')

    for r_idx in range(len(field)):

        _row = R - r_idx - 1

        r = list(field[r_idx])

        if  _row == end_point[1]:
            r[end_point[0]] = 'O'

        if _row == start_point[1]:
            r[start_point[0]] = '+'

        print(r)


    border = set()
    visited_points = set()
    rounds = 0
    
    border.add(start_point)
    visited_points.add(start_point)

    while border and  end_point not in border:
        
        _border = set() 
        for p in border:
            _border = _border | get_neighbors(p, field, visited_points)

        border = _border

        rounds +=1

    print(rounds)


if __name__ == '__main__':
    main()