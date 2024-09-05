def bin_search(arr, target):
    l,r = 0, len(arr)
    while l<=r:
        m = (l+r) // 2
        
        if m == 0 and arr[m] != target:
            return {'type': 'left_most', 'val': arr[0], 'index': 0}
        elif m > len(arr)-1:
            return {'type':'right_most', 'val': arr[-1], 'index': len(arr)-1}

        if arr[m] == target:
            return {'type':'target', 'val': arr[m], 'index': m}
        elif arr[m] < target:
            l = m+1
        else:
            r = m-1
    
    return {'type':'middle', 'val': None, 'index': (r,l)}

arr = [2, 3, 5]
print(bin_search(arr, 4))


