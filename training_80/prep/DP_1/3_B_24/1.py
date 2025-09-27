import os

def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    # filename = os.path.join(dir_name, "1.txt")
    # filename = os.path.join(dir_name, "2.txt")
    # filename = os.path.join(dir_name, "3.txt")
    # filename = os.path.join(dir_name, "4.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    queue = []
    dp = []

    for _ in range(3):
        queue.append([float('inf') for _ in range(3)])
        dp.append(0)

    for row in rows[1:]:
        queue.append(list(map(int, row.split())))
        dp.append(0)
    

    for i in range(3, len(dp)):
        dp[i] = min(dp[i-1]+queue[i][0],dp[i-2]+queue[i-1][1], dp[i-3]+queue[i-2][2] )
        
    
    print(dp[-1])
    
    

        

if __name__ == '__main__':
    main()