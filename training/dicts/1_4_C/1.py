import os
from collections import defaultdict
def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "1.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    counter = defaultdict(int)
    
    words = []
    res = []


    for row in rows:
        words += row.split()
    
    for w in words:
        res.append(counter[w])
        counter[w] +=1
    
    print(*res)

        
        
    

if __name__ == '__main__':
    main()