import os


def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    filename = os.path.join(dir_name, "1.txt")
    filename = os.path.join(dir_name, "2.txt")
    filename = os.path.join(dir_name, "3.txt")
    filename = os.path.join(dir_name, "4.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    n  = int(rows[0])
    
    dp = [0] * n
    tr = [0] * n

    def backtrack(i, dp, tr):
        
        if i == 0:
            dp[i] = 0
            return dp[i]
        
        # if dp[i] == 0:
            
        #     if (i+1) % 2 == 0:
        #         dp[i] = min(backtrack(((i+1) // 2)-1, dp), backtrack(i-1, dp))+1
        #     elif (i+1) % 3 == 0:
        #         dp[i] = min(backtrack(((i+1) // 3)-1, dp), backtrack(i-1, dp))+1
        #     else:
        #         dp[i] = backtrack(i-1, dp)+1

        if dp[i] == 0:
            
            # tr[i] = i+1

            if (i+1) % 2 == 0:

                if dp[((i+1) // 2)-1] > 0:
                    op1 = dp[((i+1) // 2)-1]
                else:
                    op1 = backtrack(((i+1) // 2)-1, dp, tr)

                if dp[i-1] > 0:
                    op2 = dp[i-1] 
                else:
                    op2 = backtrack(i-1, dp, tr)


                if op1 <= op2:
                    dp[i] = op1+1
                else:
                    dp[i] = op2+1
                
            
            elif (i+1) % 3 == 0:

                if dp[((i+1) // 3)-1] > 0:
                    op1 = dp[((i+1) // 3)-1]
                else:
                    op1 = backtrack(((i+1) // 3)-1, dp, tr)

                if dp[i-1] > 0:
                    op2 = dp[i-1] 
                else:
                    op2 = backtrack(i-1, dp, tr)


                if op1 <= op2:
                    dp[i] = op1+1
                else:
                    dp[i] = op2+1

                    
            else:
                if dp[i-1] > 0:
                    dp[i] = dp[i-1] + 1
                else:
                    dp[i] = backtrack(i-1, dp, tr)+1
        
            
        return dp[i]
        
        
    backtrack(n-1, dp, tr)

    print(dp)
    print(tr)

    

if __name__ == '__main__':
    main()