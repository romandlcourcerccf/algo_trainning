import os

def main():

    dname = os.path.dirname(__file__)

    filename = os.path.join(dname, "input.txt")
    # filename = os.path.join(dname, "2.txt")

    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]
        
    n, k  = tuple(map(int, rows[0].split()))
  
    def non_trivial_solution(n,k):

        # print(f'n {n} k {k} ')

     
        if n % 10 == 0:
            return n
        
        if n % 10 == 5:
            return n+5
        
        
        res = n
        sec = 0
        while res % 10 != 2 and sec <= k:
            # print(res % 10)
            res += res % 10
            sec +=1
            # print('>>', res)
            
        # print('res :', res)
        # print('res :', sec)

        if sec == k:
            return res
        

        _n = k-sec

        fourth_num = _n // 4
        tail = _n % 4

        # print(f'fourth_num {fourth_num} tail {tail}')

        res += fourth_num * (2+4+6+8)
        sec += fourth_num *4

        if tail:
            for r in  [2, 4, 8, 6]:
                if sec < k:
                    res += r
                    sec +=1


        return res
    
    print(non_trivial_solution(n,k))

if __name__ == "__main__":
    main()

