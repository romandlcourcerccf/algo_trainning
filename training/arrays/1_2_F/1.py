import os

def main():

    dir_name = os.path.dirname(__file__)
    # filename = os.path.join(dir_name, "input.txt")
    filename = os.path.join(dir_name, "1.txt") 
  
    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    row = rows[1]
    row = [int(n) for n in row.split()]
    
    print(row)
    
    for start in range(len(row)):

        i = start
        j = len(row)-1

        print('start :', start)

        while i < len(row) and j >= 0 and row[i] == row[j] and i <= j:
            i +=1
            j -=1
        
        print('i :', i, 'j :', j)
        if i > j:
            res = []
            for i in range(start-1, -1, -1):
                res.append(row[i])
            
            print(len(res))
            print(*res)
            return 



if __name__ == '__main__':
    main()