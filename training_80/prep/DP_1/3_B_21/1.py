import os

def main():

    dir_name = os.path.dirname(__file__)
    # filename = os.path.join(dir_name, "input.txt")
    filename = os.path.join(dir_name, "1.txt")
    # filename = os.path.join(dir_name, "2.txt")
    # filename = os.path.join(dir_name, "3.txt")
    # filename = os.path.join(dir_name, "4.txt")
    # filename = os.path.join(dir_name, "5.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]


    n = int(rows[0])

    if n < 3:
        print(2 **n)
        return
    elif n == 3:
        print(2**n-1)
    else:
        ones = 2**3-1
        for _ in range(4, n+1):
            ones = 2 * ones-1

        print(ones)
        return

    
if __name__ == '__main__':
    main()