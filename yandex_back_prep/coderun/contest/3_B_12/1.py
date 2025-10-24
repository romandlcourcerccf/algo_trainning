
import os 
dir_name = os.path.dirname(__file__)
file = os.path.join(dir_name, 'input.txt')
file = os.path.join(dir_name, '1.txt')
file = os.path.join(dir_name, '2.txt')
file = os.path.join(dir_name, '3.txt')
file = os.path.join(dir_name, '4.txt')

with open(file, 'r') as reader:
    rows = reader.readlines()
    rows = [r.rstrip() for r in rows]

# print(rows)

def val_stack(row):

    s = []

    for c in row:
        if c in ['(','[','{']:
            s.append(c)
        else:
            if not(s):
                print('no')
                return
            else:
                _c = s.pop()
                if _c+c not in ['()','[]','{}']:
                    print('no')
                    return

    print('yes' if not s else 'no')
    return
        

val_stack(rows[0])
            