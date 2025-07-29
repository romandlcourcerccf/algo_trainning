def count_sort(seq):
    min_val = min(seq)
    max_val = max(seq)

    print('min_val :', min_val)
    print('max_val :', max_val)

    k = max_val - min_val + 1

    count = [0]*k

    for s in seq:
        count[s - min_val] +=1
    
    pos = 0
    for val in range(0,k):
        for i in range(count[val]):
            seq[pos] = val + min_val
            pos +=1
  
    return seq

a = [1,1,2,3,2,4,3,4,5,4,3,5]
print(count_sort(a))
    