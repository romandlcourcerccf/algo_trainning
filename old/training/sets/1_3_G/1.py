import os

from collections import defaultdict

def to_int_array(row):
    row = row.split()
    row = [int(n) for n in row]
    return row
 
def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    
    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    
    tort_num = int(rows[0])
    tort_intervals = rows[1] 
    tort_intervals = [ tuple(map(int,row.split())) for row in rows[1:]]


    used = set()
    for i in range(tort_num):
        a, b = tort_intervals[i]
        if a >= 0 and b >= 0 and a+b == tort_num-1 and (a,b) not in used:
            used.add((a, b))

    
    print(len(used))

if __name__ == '__main__':
    main()