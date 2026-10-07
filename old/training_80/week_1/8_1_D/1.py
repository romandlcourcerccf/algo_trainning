import os

from collections import Counter 

def main():

    dname = os.path.dirname(__file__)

    filename = os.path.join(dname, "input.txt")
    # filename = os.path.join(dname, "1.txt")
    # filename = os.path.join(dname, "2.txt")
   

    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]
        
    n, k  = tuple(map(int, rows[0].split()))
    tasks = list(map(int, rows[1].split()))


    # print(f'n: {n} k: {k}')
    # print(f'tasks {tasks}')

    tasks_counter = Counter(tasks)


    sorted_tasks = sorted(list(tasks_counter.keys()))

    sorted_tasks = [ (v, k)  for  k,v in  tasks_counter.items()]
    sorted_tasks.sort()

    # print(sorted_tasks)

    res = []

    while len(res) < k:

        for t in sorted_tasks:
            if tasks_counter[t[1]] > 0:
                res.append(t[1])
                tasks_counter[t[1]] -= 1
                if len(res) == k:
                    break
    
    print(*res)

    


if __name__ == "__main__":
    main()

