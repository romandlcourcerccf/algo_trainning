import os 
dir_name = os.path.dirname(__file__)
file = os.path.join(dir_name, 'input.txt')
file = os.path.join(dir_name, '1.txt')
# file = os.path.join(dir_name, '2.txt')
# file = os.path.join(dir_name, '3.txt')
file = os.path.join(dir_name, '4.txt')
# file = os.path.join(dir_name, '5.txt')

with open(file, 'r') as reader:
    rows = reader.readlines()
    rows = [r.rstrip() for r in rows]

s1 = list(map(int, rows[1].split()))

def is_sortable(s1):
    
    s2, dd = [], []
    ln = len(s1)

    # print(len(s1))

    n = 1
    while n <= ln:

        # print(f'n : {n}')

        while len(s1) > 0 and s1[0] != n :
            # print(f's1[0] {s1[0]} s1 {s1}')
            dd.insert(0,s1.pop(0))
        
        # print(f'n {n} s1 {s1} s2 {s2} dd {dd}')

        if len(s1) == 0:
            print('NO')
            return

        if s1[0] == n:
            # print('----append----')
            # print(f'n {n}')
            # print(f'dd {dd}')

            s2.insert(0, s1.pop(0))
            n += 1
        
        while len(dd) > 0 and dd[0] == n:
            s2.insert(0,dd.pop(0))
            n+=1

    # print('dd :', dd)

    if len(dd) > 0:
        print('NO')
    else:
        print('YES')

# print(s1)
is_sortable(s1)


       
            



   
   

            