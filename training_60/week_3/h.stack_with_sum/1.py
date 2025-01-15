import sys


def main():
   
    rows = sys.stdin.readlines()

    # import os
    # dname = os.path.dirname(__file__)
    # filename = os.path.join(dname, '1.txt')
   
    # with open(filename, 'r') as f:
    #     rows = f.readlines()

    
    stack = []
    summ_st = []
    summ_st.append(0)

    for i in range(1,len(rows)):

        op = rows[i]

        if op[0] == '+':
            val = int(op[1:])
            stack.append(val)
            summ_st.append(val+summ_st[-1])

        elif op[0] == '-':
            print(stack.pop())
            summ_st.pop()
        elif op[0] == '?':
            k = int(op[1:])
            res2 = summ_st[-1] -summ_st[-(k+1)]
            print(res2)

           

if __name__ == '__main__':
    main()

