import sys


def main():
   

    # rows = sys.stdin.readlines()

    import os
    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, '1.txt')
    
    with open(filename, 'r') as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]

   
    letter = []
    for i in range(1, len(rows)):
        letter.append(rows[i])
    
    print(letter)
   
if __name__ == '__main__':
    main()
