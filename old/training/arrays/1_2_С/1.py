import os

def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    # filename = os.path.join(dir_name, "1.txt") 
  

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    row = rows[1]
    row = [int(n) for n in row.split()]
    num = int(rows[2])
    closest_numer = float('inf')

    for i in range(len(row)):
        if abs(row[i] - num) <= abs(closest_numer-num):
            closest_numer = row[i]

    print(closest_numer)
        


if __name__ == '__main__':
    main()