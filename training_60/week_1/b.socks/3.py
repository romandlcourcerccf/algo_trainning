import sys
from typing import List

def get_pair(clothes: List[int]) -> List[int]:


    A, B, C, D = clothes[0], clothes[1], clothes[2], clothes[3]

    if  A>0 and B>0 and C>0 and D>0:

        if A == B == C == D:
            return [min(A,B)+1,1]
        
        if A > B and C > D or  A < B and C < D:
            
            m1 = max(A,B)+1+1
            m2 = max(C,D)+1+1
            m3 = min(A,B)+1 + min(C,D)+1

            if min(m1, m2, m3 ) == m1:
                return [max(A,B)+1,1]
            elif min(m1, m2, m3 ) == m2:
                return [1, max(C,D)+1]
            else:
                return [min(A,B)+1,  min(C,D)+1]

        
        if A > B and C < D or  A < B and C > D: # TODO !!! CHECK !!!

            if max(A, B) + 1 + 1 < max(C, D) + 1 + 1:
                return [max(A, B)+1, 1]
            else:
                 return [1, max(C, D)+1]

            
        if A == B and A > 0 and B > 0 and C < D:
            return [min(A,B)+1, 1]
        if A == B and A > 0 and B > 0 and C > D:
            return [min(A,B)+1, 1]
        if A < B and A > 0 and B > 0 and C == D:
            return [1, min(C,D)+1]
        if A > B and A > 0 and B > 0 and C == D:
            return [1, min(C,D)+1]
        
    elif (A == B and C == 0 and D > 0) or (A == B and C > 0 and D == 0):
        return [min(A,B)+1, 1]
    elif (A == 0 and  B > 0 and C == D) or (A > 0 and B == 0 and  C == D ):
        return [1, min(C,D)+1]
    
    elif A > B and C == 0 and D > 0:
        return [max(A,B)+1,1]
    
    elif A < B and C == 0 and D > 0:
        return [min(A,B)+1,1]
    
    elif A > B and C > 0 and D == 0:
        return [min(A,B)+1,1]
    
    elif A < B and C > 0 and D == 0:
        return [max(A,B)+1,1]
    
    elif A == 0 and B > 0 and C > D:
        return [1, max(C,D)+1]
    
    elif A == 0 and B > 0 and C < D:
        return [1, min(C,D)+1]
    
    elif A > 0 and B == 0 and C > D:
        return [1, min(C,D)+1]
    
    elif A > 0 and B == 0 and C < D:
        return [1, max(C,D)+1]

   
    return [0,0]

def main():
   

    rows = sys.stdin.readlines()

    # import os
    # dname = os.path.dirname(__file__)
    # filename = os.path.join(dname, '4.txt')
    
    # with open(filename, 'r') as f:
    #     rows = f.readlines()
    #     rows = [r.rstrip() for r in rows]

    A, B, C, D = int(rows[0]), int(rows[1]), int(rows[2]), int(rows[3])

    res = get_pair([A, B, C, D])



    print(f'{res[0]} {res[1]}')

def test():

    test_cases = [
                    [[1,1,1,1],[2,1]], 
                    [[0,1,0,1],[1,1]],
                    [[1,0,1,0],[1,1]],
                    [[5,1,7,1],[2,2]],
                    [[1,5,1,7],[2,2]],
                    [[5,1,1,7],[6,1]], # !!
                    [[6,2,7,3],[3,4]],
                    [[0,2,5,1],[1,6]],
                    [[0,2,1,5],[1,2]],
                    [[2,0,5,1],[1,2]],
                    [[2,0,1,5],[1,6]],
                    [[3,3,4,7],[4,1]],
                    [[8,9,5,9],[10,1]],
                    [[412,307,241,830],[413,1]],
                    [[3,3,4,7],[4,1]],
                    [[790,493,507,302],[1,508]],
                    [[703,146,166,456],[1,508]]
                     

                  ]
    
    for i in range(len(test_cases)):
        res = get_pair(test_cases[i][0])
        if res[0] != test_cases[i][1][0] or res[1] != test_cases[i][1][1]:
            print(f'Result diff  for {test_cases[i][0]} : got {res} but expected {test_cases[i][1]}')
   
if __name__ == '__main__':

    # test()    
    main()