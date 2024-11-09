import sys


def main():
   
    # row = sys.stdin.readline()

    import os
    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, '7.txt')
   
    with open(filename, 'r') as f:
        row = f.readline()
    
    left = ['(', '[', '{']
    pairs = ['()', '[]', '{}']

    stack = []

    for p in row:
       if p in left:
           stack.append(p)
       else:
           if not stack:
               print('no')
               break
           _p = stack.pop()
           if _p+p not in pairs:
                print('no')
                break

    print('yes') if not stack else print('no')
    


if __name__ == '__main__':
    main()