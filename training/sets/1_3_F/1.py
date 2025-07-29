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


    row_1 = rows[0]
    row_2 = rows[1]


    S_2 = set()
    for i in range(0, len(row_2)-1, 1):
        S_2.add(row_2[i:i+2])

    count = 0
    for i in range(0, len(row_1)-1, 1):
        if row_1[i:i+2] in S_2:
            count +=1
            
    
    print(count)
    

if __name__ == '__main__':
    main()