import os

        
def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    # filename = os.path.join(dir_name, "1.txt")
    filename = os.path.join(dir_name, "2.txt")
    # filename = os.path.join(dir_name, "3.txt")
    # filename = os.path.join(dir_name, "4.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]
 
    nails = list(map(int, rows[1].split()))
    # print(nails)
    nails.sort()
    # print(nails)
    
    acc_dist = 0 
    i = 1
    pairs = []
    
    while i <= len(nails)-1:
        
        if i == 1 or i == len(nails)-1:
            acc_dist += abs(nails[i-1] - nails[i])
            pairs.append([nails[i-1], nails[i]])
        else:
            if abs(nails[i-1] - nails[i]) <= abs(nails[i] - nails[i+1]):
                acc_dist += abs(nails[i-1] - nails[i])
                pairs.append([nails[i-1], nails[i]])
        
        i +=1

    # print(pairs)

    print(acc_dist)
    

if __name__ == '__main__':
    main()