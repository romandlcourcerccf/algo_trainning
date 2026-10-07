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

    h = defaultdict(int)
    ch_num = int(rows[0])
   
    for r in rows[1:]:
        if not r.isdigit():
            h[r] +=1
    
    
    ubic_lang = []
    other_lang = []

    for k,v in h.items():
        if v == ch_num:
            ubic_lang.append(k)
        else:
            other_lang.append(k)
    
    print(len(ubic_lang))
    for l in ubic_lang:
        print(l)
    
    print(len(other_lang+ubic_lang))
    for l in other_lang+ubic_lang:
        print(l)

if __name__ == '__main__':
    main()