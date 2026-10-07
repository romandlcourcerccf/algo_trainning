import os

def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "1.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    row = rows[1]
    row = [int(n) for n in row.split()]
    
    max_idx  = []
    max_val = float('-inf')
    for i in range(len(row)):
        if row[i] >= max_val:
            max_val = row[i]
            max_idx.append(i)
    
    res_idx = -1
    max_idx = max_idx[0]
   
    for i in range(len(row)-1):
        if i < max_idx:
            continue
        if row[i] % 5 == 0 and row[i+1] < row[i]:
            res_idx = i
    
    count_more = 0
    for i in range(len(row)):
        if i < res_idx and row[i] > row[res_idx]:
            count_more +=1
    

    if res_idx != -1:
         print(count_more+1)
    else:
        print(0)
        


if __name__ == '__main__':
    main()