arr = [7, 2, 4, 5, 3, 2, 5, 1, 5]
res = [0] * len(arr)
st = []


for i, v in enumerate(arr):
    if i == 0:
        st.append((i, v))
    else:
        while st and v > st[-1][1]:
            res[st[-1][0]] = i
            st.pop()

    st.append((i, v))


print(res)
