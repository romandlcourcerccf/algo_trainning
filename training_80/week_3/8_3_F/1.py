import os
from collections import defaultdict

def main():

    dname = os.path.dirname(__file__)

    filename = os.path.join(dname, "input.txt")
    filename = os.path.join(dname, "1.txt")
    # filename = os.path.join(dname, "2.txt")
    # filename = os.path.join(dname, "3.txt")
    
    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]
    
    tree = defaultdict(set)

    nodes = map(int, rows[1].split())
    for i, v in enumerate(nodes):
        tree[v].add(i+1)

    
    class ParentChecker:
        def __init__(self, tree):
            self.tree = tree
            self.is_parent = False

        def dfs(self, root, track, target, parent):

            if not root in self.tree:
                return
        
            if root == target and parent in track:
                self.is_parent = True
                return

            for child in self.tree[root]:
                self.dfs(child, track.copy().add(root), target, parent)

        
        def is_parent(self):
            return self.is_parent

    






    

    # class PathFinder:
    #     def __init__(self, tree):
    #         self.min_path = float('inf')
    #         self.tree = tree
        
    #     def dfs(self, root):

    #         if root not in tree:
    #             return 1
        
    #         p_lens = []
    #         for c in  tree[root]:
    #             p_lens.append(self.dfs(c))

    #         if len(p_lens) > 1:
    #             self.min_path = min(self.min_path, sum(p_lens))
        
    #         return min(p_lens) + 1
    
    # pf = PathFinder(tree)
    # print(pf.dfs(1))

    # print(f'min_path {pf.min_path}')
        

if __name__ == "__main__":
    main()

   


