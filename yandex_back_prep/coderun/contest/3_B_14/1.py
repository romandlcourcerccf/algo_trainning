import os 
dir_name = os.path.dirname(__file__)
file = os.path.join(dir_name, 'input.txt')
file = os.path.join(dir_name, '1.txt')
file = os.path.join(dir_name, '2.txt')
# file = os.path.join(dir_name, '3.txt')
# file = os.path.join(dir_name, '4.txt')
# file = os.path.join(dir_name, '5.txt')

with open(file, 'r') as reader:
    rows = reader.readlines()
    rows = [r.rstrip() for r in rows]

s1 = list(map(int, rows[1].split()))

def is_sortable(s1):

    s2 = []
    dend = []

    n=1
    while n <= len(s1):
        print('n :', n)
        while len(s1) !=0 and s1[0] != n:
            print(">>>>>",s1[0])
            dend.append(s1.pop(0))
           
            if len(s1)==0:
                break
        
        print('n : ',n, 'dend :', dend )
        s2.append(s1.pop(0))
        n+=1

        while len(dend) !=0  and dend[0] == n:
            s2.append(dend.pop(0))
            n+=1

    print('>>')
    print('s1 >>',s1)
    print('s1 >>',s2)
    print('dend >>',dend)
    print('YES' if len(dend) == 0 else 'NO')

print(s1)
is_sortable(s1)


       
            



   
   

            