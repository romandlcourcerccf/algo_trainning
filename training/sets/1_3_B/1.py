import os
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

    row1 = to_int_array(rows[0])
    row2 = to_int_array(rows[1])

    res = list(set(row1).intersection(row2))
    res.sort()

    print(*(res))


if __name__ == '__main__':
    main()