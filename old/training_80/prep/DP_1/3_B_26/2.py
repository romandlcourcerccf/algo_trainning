import os
from collections import defaultdict

def get_closest_point(idx, nails):

    min_dist = float('inf')
    closest_point = None

    for i in range(len(nails[:idx])):
        if abs(idx - nails[i]) <= min_dist:
            min_dist = abs(idx - nails[i])
            closest_point = i

    return closest_point

def remove_with_max_dist()
     
def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    filename = os.path.join(dir_name, "1.txt")
    # filename = os.path.join(dir_name, "2.txt")
    # filename = os.path.join(dir_name, "3.txt")
    # filename = os.path.join(dir_name, "4.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]
 
    nails = list(map(int, rows[1].split()))
    
    acc_dist = 0 
    pairs = defaultdict(set)
    
    for idx in range(1, len(nails)):
    
        closest_point, closest_dist = get_closest_point(idx, nails)

        if closest_point not in pairs:
            pairs[closest_point].add(nails[idx])
            acc_dist += closest_dist
        else:
            for p in pairs[closest_point]:
                
        
        


if __name__ == '__main__':
    main()