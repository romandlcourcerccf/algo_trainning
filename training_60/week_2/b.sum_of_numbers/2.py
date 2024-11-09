def main():

    # rows = sys.stdin.readlines()

    import os
    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, '2.txt')
   
    with open(filename, 'r') as f:
        rows = f.readlines()

    _,k = tuple(map(int, rows[0].split()))
    nums = list(map(int, rows[1].split()))

    print(f'n : {_} k   :{k}')
    print(f'nums:{nums}')

    cnt = {0:1}
    now_sum = 0
    ans = 0
    for now in nums:
        now_sum += now
        ans += cnt.get(now_sum-k,0)
        cnt[now_sum] = cnt.get(now_sum, 0)+1
    
    print(ans)

if __name__ == '__main__':
    main()