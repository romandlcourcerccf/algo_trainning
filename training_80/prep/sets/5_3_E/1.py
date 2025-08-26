import os

from collections import Counter

def main():

    dir_name = os.path.dirname(__file__)
    # filename = os.path.join(dir_name, "input.txt")
    filename = os.path.join(dir_name, "1.txt")
    # filename = os.path.join(dir_name, "2.txt")
    # filename = os.path.join(dir_name, "3.txt")
    # filename = os.path.join(dir_name, "7.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    
    set1 = set(map(int, rows[1].split()))
    set2 = set(map(int, rows[3].split()))
    set3 = set(map(int, rows[5].split()))

   
    print(*sorted(list((set1 & set2) | (set2 & set3) | (set1 & set3))))

if __name__ == '__main__':
    main()