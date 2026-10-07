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
    
    dp[1] = 0

    for i in range(2, n):
        dp[i] = min(dp[i-1], dp[int(i/2)] if i // 2 == 0 else float('inf'), dp[int(i/3)] if i // 3 == 0 else float('inf') )+1


    back_track = [n]

    while back_track[-1] != 1:

        last = back_track[-1]

        print(last)

        if last % 3 == 0 and dp[int(last / 3)] == dp[last]-1:
            back_track.append(int(last / 3))
        elif last % 2 == 0 and dp[int(last / 2)] == dp[last]-1:
            back_track.append(int(last / 2))
        else:
            back_track.append(last-1)

    print(dp)
    print(back_track)
   

   
    

if __name__ == '__main__':
    main()