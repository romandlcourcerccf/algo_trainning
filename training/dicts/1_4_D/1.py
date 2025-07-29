import os
from collections import defaultdict
def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    keys = list(map(int, rows[1].split()))
    pressed_history = list(map(int, rows[3].split()))
    press_counter = defaultdict(int)
    
    # print(keys)
    # print(pressed_history)

    for p in pressed_history:
        press_counter[p] +=1
    
    # print(press_counter)
        
    for k in range(len(keys)):
        if keys[k] < press_counter[k+1]:
            print('YES')
        else:
            print('NO')
    

if __name__ == '__main__':
    main()