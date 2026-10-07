import os
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)


def dfs(employeee, tree, income):

    if not tree[employeee]:
        income[employeee]+=1
        employeee
        return 1
    
    child = min(tree[employeee])

    _income = dfs(child, tree, income)
    
    if _income == 1:
        tree[employeee].remove(child)
        if len(tree[employeee]) == 0:
            del tree[employeee]

    _income +=1  
    income[employeee] += _income

    return _income


def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    # filename = os.path.join(dir_name, "1.txt")
    filename = os.path.join(dir_name, "2.txt")
    # filename = os.path.join(dir_name, "31.txt")
    filename = os.path.join(dir_name, "35.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    mun_of_employees = int(rows[0])
    employees = list(map(int, rows[1].split()))


    tree = defaultdict(set)
    income = defaultdict(int)

    for index, employee in enumerate(employees):
        tree[employee].add(index+2)


    while(len(tree[1]) > 0):
        dfs(1, tree, income)

    income[1]+=1


    res = []
    for employee_num  in range(mun_of_employees):
        res.append(income[employee_num+1])
       
    print(*res) 
    
if __name__ == '__main__':
    main()