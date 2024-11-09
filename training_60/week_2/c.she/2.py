import sys


def main():
   
    # rows = sys.stdin.readlines()

    import os
    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, '1.txt')
   
    with open(filename, 'r') as f:
        rows = f.readlines()
    
    n, r = list(map(int, rows[0].split()))
    arr = list(map(int, rows[1].split()))
    
    print(f'n  : {n} r {r}')
    print(f'arr {arr}')

    ans, left, right = 0, 0, 0

    while left < n and right < n:
        while right < n and arr[right] - arr[left] <= r:
            right +=1
        ans += n - right
        left += 1
    
    print(ans)
  
    
   
if __name__ == '__main__':
    main()
