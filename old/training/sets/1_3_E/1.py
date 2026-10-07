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


     
    row_1 = set(rows[0].split())
    row_2 = set(list(rows[1]))

    print(len(row_2 - row_1))


    
    
    


if __name__ == '__main__':
    main()