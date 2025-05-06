def bin_search(arr, n):

    l,r = 0, len(arr)

    while l < r:
        m = (l+r) // 2
        if n == arr[m]:
            return True
        elif n < arr[m]:
            r = m
        else:
            l = m+1

    return False

arr = [1, 61, 126, 217, 2876, 6127, 39162, 98126, 712687, 1000000000]
N = 1000000000

print(bin_search(arr, N))