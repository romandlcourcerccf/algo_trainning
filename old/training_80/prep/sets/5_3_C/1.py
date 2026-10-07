import os

from collections import Counter

def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    # filename = os.path.join(dir_name, "1.txt")
    filename = os.path.join(dir_name, "3.txt")
    filename = os.path.join(dir_name, "7.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    row = list(map(int,rows[1].split()))
    counter = Counter(map(int,row))
    
    numbers = list(counter.keys())
    numbers.sort()
    print(numbers)

    res = 0
    for i in range(len(numbers)-1, -1, -1):
        if abs(numbers[i] - numbers[0]) > 1:
            res += counter[numbers[i]]
    
    print(res)
    

if __name__ == '__main__':
    main()