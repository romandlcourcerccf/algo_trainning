import os

def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    # filename = os.path.join(dir_name, "1.txt")
    # filename = os.path.join(dir_name, "2.txt")
    # filename = os.path.join(dir_name, "3.txt")
    # filename = os.path.join(dir_name, "4.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    n  = int(rows[0])
    
    
    hist = []
    ops = 0
    i = 1 
    hist.append(i)

    while i < n:
        
        if i*3 <= n:
            i = i*3
            hist.append(i)
            ops+=1
            continue

        if i*2 <= n:
            i = i*2
            hist.append(i)
            ops+=1
            continue

        if i+1 <=n:
            i = i+1
            hist.append(i)
            ops+=1
            continue
    
    print(ops)
    print(*hist)

        

if __name__ == '__main__':
    main()