import sys
import os
from collections import Counter

# TODO Do this effective!
def calc_load(arrivels_count, count_times, capasity):

    load_result = [0]*len(arrivels_count)
    for i in range():
        

def main():


    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "2.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        
    # rows = sys.stdin.readlines()
   
    
    t_num, h_cup = tuple(map(int, rows[0].split()))
    print(f't_num {t_num} h_cup {h_cup}')

    arr_times = [int(r) for r in rows[1:]]
    arr_times.sort()
    print('arr_times :', arr_times)

    count_times = Counter(arr_times)
    print('acc_arr_times',count_times)

    arr_times_acc = [0] * len(arr_times)
    for i in range(len(arr_times)):
        if i in count_times:
            arr_times_acc[i] = count_times[i]
    
    print('arr_times_acc',arr_times_acc)
    
    res_time = -1
    res_acc = None

    l, r = 0, len(arr_times)
    while l < r:
        stay_time = (l+r) // 2
    
        acc_times = [0]*len(arr_times)
        for i in range(0,len(acc_times)):
            acc_times[i] = sum(arr_times_acc[max(0, i-stay_time+1):i+1])

        max_fill = max(acc_times)
        print(f'max_fill {max_fill}, acc_times : {acc_times}')
        if max_fill > h_cup:
            r = stay_time -1
        elif max_fill < h_cup:
            l = stay_time +1
        else:
            res_time = stay_time
            res_acc = acc_times
            break

    print('res_time :',res_time)
    print('res_acc  :',res_acc)
        


    

        
        
        




if __name__ == '__main__':
    main()