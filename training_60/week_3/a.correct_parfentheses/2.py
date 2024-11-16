import sys

op = {'(', '[', '{'}
comp = {'()', '[]', '{}'}

def is_valid(row):

    h = []
    for c in row:
        if c in op:
            h.append(c)
        else:
            if len(h) == 0:
                return "no"
            
            _c = h.pop()
            if _c+c not in comp:
                return "no"

    if  len(h) == 0:
        return "yes"
    
    return "no"
    
row = sys.stdin.readline()

# import os
# dname = os.path.dirname(__file__)
# filename = os.path.join(dname, '7.txt')
   
# with open(filename, 'r') as f:
#     row = f.readline()

# row = row.rstrip()

print(is_valid(row))

    
