import os

def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    # filename = os.path.join(dir_name, "1.txt")
    # filename = os.path.join(dir_name, "2.txt")
    # filename = os.path.join(dir_name, "3.txt")
    #filename = os.path.join(dir_name, "4.txt")
    # filename = os.path.join(dir_name, "5.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]


    n = int(rows[0])
   
    if n == 0:
        print(0)
    else:
        dp0, dp1, dp2 = 1, 1, 0

        for i in range(2, n+1):
            _dp0 = dp0 + dp1 + dp2
            _dp1 = dp0 
            _dp2 = dp1
            dp0, dp1, dp2  = _dp0, _dp1, _dp2 
    

        print(dp0 + dp1 + dp2)

    
if __name__ == '__main__':
    main()