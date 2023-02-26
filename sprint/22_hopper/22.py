def hopper(N, k):
    ans = 0

    steps = [0] * N
    steps[0] = 1

    for i in range(1, N):
        if i <= k:
            steps[i] = sum(steps[0:i])
        else:
            steps[i] = sum(steps[i-k:i])

    return steps[-1]

if __name__  == '__main__':

   
    N, k = open('input.txt', 'r').read().split(' ')
    N, k = int(N), int(k)

    variants = hopper(N,k)

    open('output.txt', 'w').write(str(variants))

   

