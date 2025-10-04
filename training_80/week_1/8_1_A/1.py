import os

import itertools
from random import randrange


class TestDataIterator:

    def __init__(self, max_val:int, max_len:int, seq_len:int):

        self.max_val = max_val
        self.max_len = max_len
        self.seq_len = seq_len

        self._sequence = self._gen_data()
        self._index = 0


    def _gen_data(self):

        sequence = []

        for _ in range(self.seq_len):
            sequence.append([randrange(self.max_val) for i in range(randrange(2, self.max_len))])

        return sequence


    def __next__(self):
        if self._index < len(self._sequence):
            item =  self._sequence[self._index]
            self._index +=1
            return item
        else:
            raise StopIteration
        

    def __iter__(self):
        return self
    



def main():

    dname = os.path.dirname(__file__)

    filename = os.path.join(dname, "input.txt")
    filename = os.path.join(dname, "1.txt")
    # filename = os.path.join(dname, "2.txt")
    # filename = os.path.join(dname, "4.txt")
    # filename = os.path.join(dname, "5.txt")
    filename = os.path.join(dname, "6.txt")
    # filename = os.path.join(dname, "7.txt")
    filename = os.path.join(dname, "8.txt")


    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]
        
    mashrooms = list(map(int,rows[1].split()))

    # print(mashrooms)


    
    def trivial_solution(mashrooms):

        max_hap = float('-inf')
        max_i = -1
        max_j = -1

        for i in range(len(mashrooms)):
            for j in range(len(mashrooms)):
                if i != j:
                    mashrooms[i], mashrooms[j] = mashrooms[j], mashrooms[i]

                    v = mashrooms[::2]
                    m = mashrooms[1::2]

                    if sum(v) - sum(m) > max_hap:
                        max_hap = sum(v) - sum(m)
            
                        max_j = i
                        max_i = j

                    mashrooms[j], mashrooms[i] = mashrooms[i], mashrooms[j]

    
        print('Trivial:')    
        print(f' idx_1 {max_i} {mashrooms[max_i]}')
        print(f' idx_2 {max_j} {mashrooms[max_j]}')

   
        return max_hap
    
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
    
    print('>>',mashrooms)
    n_tr_sol  = non_trivial_solution(mashrooms.copy())
    print('>>',mashrooms)
    tr_sol = trivial_solution(mashrooms.copy())
    print('>>',mashrooms)

    print('non triv:', n_tr_sol)
    print('tr_sol  :', tr_sol)

    # tdi = TestDataIterator(max_val=100, max_len=20, seq_len=1000)

    # bad_cases = []
    # for d in tdi:
    #     print(d)
    #     _tr = trivial_solution(d.copy())
    #     _nt = non_trivial_solution(d.copy())


    #     if _tr != _nt:
    #         print('data : ', d)
    #         print('trivial : ', _tr)
    #         print('nontrivial : ', _nt)

    #         bad_cases.append({'data': d, 'trivial': _tr, 'nontrivial': _nt })


    # for bc in bad_cases:
    #     print(bc)

# {'data': [42, 45, 90, 8, 92, 21, 53], 'trivial': 209, 'nontrivial': 203}
#{'data': [60, 5, 84, 19, 56, 18, 29], 'trivial': 187, 'nontrivial': 167}

if __name__ == "__main__":
    main()

   


