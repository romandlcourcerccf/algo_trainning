import os
def to_int_array(row):
    row = row.split()
    row = [int(n) for n in row]
    return row
 
def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    
    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

        int_rep = []
        for row in rows:
            int_rep.append(to_int_array(row))

    # print(int_rep)
    
    set_1_sz, set_2_sz  = int_rep[0][0], int_rep[0][1]
    cubicles = [c[0] for c in int_rep[1:]]

    # print('s1 :', set_1_sz)
    # print('s2 :', set_2_sz)

    # print(cubicles)

    cubicles1 = cubicles[:set_1_sz]
    cubicles2 = cubicles[set_1_sz:]

    # print('cubicles1 :', cubicles1)
    # print('cubicles2 :', cubicles2)

    intersect = set(cubicles1).intersection(set(cubicles2))
    print(len(intersect))
    print(*sorted(list(intersect)))
    
    diff  = set(cubicles1) - set(cubicles1).intersection(set(cubicles2))
    print(len(diff))
    print(*sorted(list(diff)))
    
    diff  = set(cubicles2) - set(cubicles2).intersection(set(cubicles1))
    print(len(diff))
    print(*sorted(list(diff)))


    


if __name__ == '__main__':
    main()