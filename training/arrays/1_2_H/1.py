import os

def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt") 
    # filename = os.path.join(dir_name, "1.txt") 
  
    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    row = rows[0]
    row = [int(n) for n in row.split()]

    row.sort()
    print(row)

    if row[-1]*row[-2]*row[-3] > row[0]*row[-2]*row[-1]:
        print(*[row[-1],row[-2],row[-3]])
    else:
        print(*[row[0],row[-2],row[-1]])


if __name__ == '__main__':
    main()