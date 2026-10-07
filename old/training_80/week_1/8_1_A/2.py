import os

def main():

    dname = os.path.dirname(__file__)

    filename = os.path.join(dname, "input.txt")
    # filename = os.path.join(dname, "1.txt")
    # filename = os.path.join(dname, "2.txt")
    # filename = os.path.join(dname, "4.txt")
    # filename = os.path.join(dname, "5.txt")


    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]
        
    mashrooms = list(map(int,rows[1].split()))

   
    def non_trivial_solution(mashrooms):
        
        v = mashrooms[::2]
        m = mashrooms[1::2]

        orig_val = sum(v) - sum(m)

        
        max_m = float('-inf')
        min_v = float('inf')

        arg_max_m = -1
        arg_min_v = -1

        m_set = []
        v_set = []

    
        for i in range(len(mashrooms)):

            if i%2 != 0:
    
                if mashrooms[i] >= max_m:
                    max_m = mashrooms[i]
                    arg_max_m = i
                m_set.append(mashrooms[i])
            
            if i%2 == 0:
                if mashrooms[i] <= min_v:
                    min_v = mashrooms[i]
                    arg_min_v = i
                v_set.append(mashrooms[i])

        mashrooms[arg_min_v], mashrooms[arg_max_m]  = mashrooms[arg_max_m], mashrooms[arg_min_v]

        v = mashrooms[::2]
        m = mashrooms[1::2]

        res_val = sum(v) - sum(m) 

        return res_val if res_val > orig_val else orig_val

    print(non_trivial_solution(mashrooms))


    

if __name__ == "__main__":
    main()

