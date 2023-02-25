def min_left(arr):
    res = [0] * len(arr)
    st = []
    for i in range(len(arr)):

        while len(st) > 0:
            cur = st.pop()
            if cur[0] > arr[i]:
                res[cur[1]] = i
            else:
                st.append(cur)
                break
        
        st.append((arr[i], i))
        
    while len(st) > 0:
        cur = st.pop()
        res[cur[1]] = len(res)

    print('>>',st)

    return res    

if __name__ == '__main__':
    arr = [7,2,4,5,3,2,5,1,5,4]
    print(min_left(arr))

