import sys
from collections import defaultdict

import sys

sys.setrecursionlimit(100000)

def main():
   
    # rows = sys.stdin.readlines()

    import os
    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, '2.txt')
   
    with open(filename, 'r') as f:
        rows = f.readlines()
    
    hierachy = defaultdict(set)
  
    emp_num = int(rows[0])
    print('emp_num :',emp_num)

    bosses = list(map(int, rows[1].split()))
    bonuses = [0]*(emp_num)

    for i in range(2, emp_num+1):
        hierachy[int(bosses[i-2])].add(i) 

    def dfs(root):

        if root not in hierachy or len(hierachy[root]) == 0:
           
            for k in hierachy:
                if root in hierachy[k]:
                    hierachy[k].remove(root)

            bonuses[root-1] +=1
            
            return 1
        else:
            print('hierachy[root]' ,hierachy[root])
            _min = min(hierachy[root])
            prise = 1 + dfs(_min)
            bonuses[root-1] += 1
            return prise

   
   
    while hierachy[1]:
        bonuses[0] += dfs(1)
   
    bonuses[0] +=1
    print('bonuses:', bonuses)

    

    
   

if __name__ == '__main__':
    main()
