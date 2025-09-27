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

def get_closest(n:int, used:set) -> int:

    closest = None
    closest_dist = float('inf')

    for u in used:
        if abs(u - n) <= closest_dist:
            closest_dist = abs(u - n)
            closest = u

    return closest, closest_dist

def get_min_max_dist(connect_info, closest):

    min_dist_neigbour = float('inf')
    closest_neigbour = None

    max_dist_neigbour = float('inf')
    fathest_neigbour = None

    for neigbour in connect_info[closest]:
        if abs(neigbour - closest) <= min_dist_neigbour:
            min_dist_neigbour = abs(neigbour - closest)
            closest_neigbour = neigbour

        if abs(neigbour - closest) >= max_dist_neigbour:
            max_dist_neigbour = abs(neigbour - closest)
            fathest_neigbour = neigbour

    return closest_neigbour,  min_dist_neigbour, fathest_neigbour, max_dist_neigbour
    
def purge_connection(connect_info, closest:int, closest_neigbour:int, used:set):

    connect_info[closest].remove(closest_neigbour)
    connect_info[closest_neigbour].remove(closest)

def main():

    dir_name = os.path.dirname(__file__)
    # filename = os.path.join(dir_name, "input.txt")
    filename = os.path.join(dir_name, "1.txt")
    # filename = os.path.join(dir_name, "2.txt")
    # filename = os.path.join(dir_name, "3.txt")
    # filename = os.path.join(dir_name, "4.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]
 
    nails = list(map(int, rows[1].split()))
    
    # print(nails)

    connect_info = defaultdict(set)
    used = set()
    connectivity_sum = 0

    for n in nails:

        closest, closest_dist  = get_closest(n, used)
        # print(f'n {n}  closest {closest}, closest_dist {closest_dist}')
        # print(connect_info)

        if len(used) == 0:
            used.add(n)
        elif len(used) == 1:
            used.add(n)

            connect_info[closest].add(n)
            connect_info[n].add(closest)
            connectivity_sum += closest_dist

        else:
            
            closest_neigbour,  min_dist_neigbour, fathest_neigbour, max_dist_neigbour =  get_min_max_dist(connect_info, closest)

            used.add(n)

            connect_info[closest].add(n)
            connect_info[n].add(closest)
            connectivity_sum += closest_dist

            
            if closest_neigbour and min_dist_neigbour >  closest_dist:

                purge_connection(connect_info, closest, closest_neigbour, used)
                connectivity_sum -= min_dist_neigbour

                if len(connect_info[closest_neigbour])==0:
                    _closest, _closest_dist  = get_closest(closest_neigbour, used)

                    connect_info[_closest].add(closest_neigbour)
                    connect_info[closest_neigbour].add(_closest)
                    connectivity_sum += _closest_dist
            
      
        # print(connect_info)
        # print(f'connectivity_sum : {connectivity_sum}')
    print(connectivity_sum)


if __name__ == '__main__':
    main()