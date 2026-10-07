import os

def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    
    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    N, K = tuple(map(int, rows[0].split()))
    nums = list(map(int, rows[1].split()))

    # print('K :',K)
    # print('nums :',nums)

    prefix = [0] * (N + 1)

    prefix[1] = nums[0]

    for i in range(1, N+1):
        prefix[i] = prefix[i-1] + nums[i-1]

    # print('prefix :', prefix)
    
    counter = 0
    l = r = 0 
    
    while r <= N:
        diff = prefix[r] - prefix[l]
        if diff == K:
            # print('l :', l+1, 'r :', r)

            counter +=1
            r +=1
        elif diff < K:
            r +=1
        elif diff > K:
            l +=1
    
    print(counter)

    


if __name__ == '__main__':
    main()