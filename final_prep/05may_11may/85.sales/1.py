import sys
import os

def main():


    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "3.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
    
   
    products = {}

    for row in rows:
        row = row.split()
        _name, _type, _quantity =  row[0] , row[1], row[2]
        if _name not in products:
            products[_name] = {}
        
        _name_table = products[_name] 

        if _type not in _name_table:
            _name_table[_type] = 0

        _name_table[_type] += int(_quantity)

    
    for name in sorted(list(products.keys())):
        print(f'{name}:')
        for product in sorted(list(products[name].keys())):
            print(f'{product} {products[name][product]}')
   


        
        
        




if __name__ == '__main__':
    main()