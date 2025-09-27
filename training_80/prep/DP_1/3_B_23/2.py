import os

def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    filename = os.path.join(dir_name, "1.txt")
    filename = os.path.join(dir_name, "2.txt")
    # filename = os.path.join(dir_name, "3.txt")
    # filename = os.path.join(dir_name, "4.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    n  = int(rows[0])
    
    dp = [0] * (n)
    track = [0] * (n)
    
    def back_track(i, dp, track):

        if dp[i] > 0:
            return dp[i] 

        if i == 0:
            dp[i] = 0
            track[i] = 1
            return dp[i] 
            
        if dp[i] == 0:
           
            if i+1 % 2:
                b1 = back_track(int(i/2), dp, track)+1
                b2 = back_track(i-1, dp, track)+1
                if b1 < b2:
                    dp[i] = b1 
                    track[i] = (i)*track[int(i/2)]
                else:
                    dp[i] = b2
                    track[i] = (i)+track[i-1]
                   
            elif i % 3:
                b1 = back_track(int(i/3), dp, track)+1
                b2 = back_track(i-1, dp, track)+1
                if b1 < b2:
                    dp[i] = b1 
                    track[i] = (i)*track[int(i/3)]
                else:
                    dp[i] = b2
                    track[i] = (i)+track[i-1]
                  
            else:
                dp[i] =  back_track(i-1)+1
                track[i] = (i)+track[i-1]
                
        return dp[i] 

    back_track(len(dp)-1, dp, track)

    print(dp)
    # print(track)
        


if __name__ == '__main__':
    main()