import sys

# class TreeNode():
#     def __init__(self, 
#                  val: str, 
#                  depth:int,
#                  left=None, 
#                  right=None,
#                  ):
#         self._val = val
#         self._left = left
#         self._right = right
#         self._depth = depth


# def fill_up(root: TreeNode, val, depth):



def main():
   
    rows = sys.stdin.readlines()

    # import os
    # dname = os.path.dirname(__file__)
    # filename = os.path.join(dname, '3.txt')
   
    # with open(filename, 'r') as f:
    #     rows = f.readlines()
    
    hierachy = {}
    nodes_set = set()
   
    for row in rows[1:]:
        row = row.split()
        nodes_set.add(row[0])
        nodes_set.add(row[1])
        hierachy[row[0]] = row[1]
    
    res = []

    for node in nodes_set:
        depth = -1
        cur = node
        while cur:
            depth +=1
            if cur in hierachy:
                cur = hierachy[cur]
            else:
                break

        res.append((node,depth))

    res.sort(key=lambda x: x[0])
    
    for r in res:
        print(f'{r[0]} {r[1]}')

if __name__ == '__main__':
    main()
