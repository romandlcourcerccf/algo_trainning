import os
from random import randrange

class TestDataIterator:

    def __init__(self, min_val:int, max_val:int, max_sec_elapsed:int, seq_len:int):

        self.max_val = max_val
        self.min_val = min_val
        self.max_sec_elapsed = max_sec_elapsed
        self.seq_len = seq_len
       
        self._sequence = self._gen_data()
        self._index = 0


    def _gen_data(self):

        sequence = []

        for _ in range(self.seq_len):
            start_time = randrange(self.min_val, self.max_val)
            sec_elapsed = randrange(start_time, self.max_sec_elapsed)
            sequence.append((start_time, sec_elapsed))

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
    # filename = os.path.join(dname, "3.txt")
    filename = os.path.join(dname, "3.txt")
    filename = os.path.join(dname, "5.txt")
    filename = os.path.join(dname, "6.txt")
    filename = os.path.join(dname, "4.txt")
    filename = os.path.join(dname, "7.txt")
    filename = os.path.join(dname, "8.txt")
   

    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]
        
    n, k  = tuple(map(int, rows[0].split()))
  
    # print(f'n: {n} k: {k}')

    def trivial_solution(n,k):

        print(f'n: {n} k: {k}')
   
        for _ in range(k):

            # print(n % 10)
            n += n % 10
            # print('n :',n)

        return n


    def non_trivial_solution(n,k):

        
        if n % 10 == 0:
            return n
        
        if n % 10 == 5:
            return n+5
        
        res = n
        sec = 0
        while res % 10 != 2 and sec <= k:
            res += res % 10
            sec +=1
    
        if sec == k:
            return res
        

        _n = k-sec

        fourth_num = _n // 4
        tail = _n % 4

        res += fourth_num * (2+4+6+8)
        sec += fourth_num *4

        if tail:
            for r in  [2, 4, 8, 6]:
                if sec < k:
                    res += r
                    sec +=1


        return res
    

    print('trivial :',trivial_solution(n,k))
    print('non trivial :', non_trivial_solution(n,k))

    tdi = TestDataIterator(min_val=0, max_val=10, max_sec_elapsed=50, seq_len=100000)

    bad_cases = []
    for d in tdi:
        print(d)
        _tr = trivial_solution(*d)
        _nt = non_trivial_solution(*d)


        if _tr != _nt:
            print('data : ', d)
            print('trivial : ', _tr)
            print('nontrivial : ', _nt)

            bad_cases.append({'data': d, 'trivial': _tr, 'nontrivial': _nt })


    for bc in bad_cases:
        print(bc)


if __name__ == "__main__":
    main()

