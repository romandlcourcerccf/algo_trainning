import os
from collections import defaultdict
def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "3.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

   
    name_prod__q_h = defaultdict(int)
    name_prod_h = defaultdict(set)



    for r in rows:
        name, priduct, ktu = tuple(r.split()) 
        name_prod__q_h[name + '_'+priduct] += int(ktu)
        name_prod_h[name].add(priduct)


    print(name_prod_h)

    for name in name_prod_h:
        print(name+':')
        for product in  sorted(name_prod_h[name]):
            print(product, name_prod__q_h[name+'_'+product])


if __name__ == '__main__':
    main()
