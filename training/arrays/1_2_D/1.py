import os

def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    # filename = os.path.join(dir_name, "2.txt") 
  

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]


    row = rows[0]
    row = [int(n) for n in row.split()]

    counter = 0
    
    for i in range(1, len(row)-1):
        if row[i-1]<row[i] and row[i]>row[i+1]:
            counter +=1
    
    print(counter)


if __name__ == '__main__':
    main()