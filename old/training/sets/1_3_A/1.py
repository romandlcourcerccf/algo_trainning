import os

def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    
    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    row = rows[0]
    row = row.split()
    row = [int(n) for n in row]
    
    print(len(set(row)))


if __name__ == '__main__':
    main()