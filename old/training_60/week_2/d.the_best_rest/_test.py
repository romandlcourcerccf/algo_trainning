arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = [4, 2, 1]


k = 2

counter = 0
_c = 0
while len(arr) > 0 and abs(arr[-1] - arr[0] > k):
    # print('arr :',arr)

    counter += 1

    l, r = 0, len(arr) - 1
    jobs_done = set()

    while l < r and abs(arr[l] - arr[r]) >= k:
        jobs_done.add(l)
        jobs_done.add(r)

        _l, _r = l, r
        # print(f' _l, _r  {_l}, {_r}')
        while abs(arr[l] - arr[_l]) < k and _l < len(arr) - 1:
            _l += 1

        while abs(arr[r] - arr[_r]) < k and _r > 0:
            _r -= 1

        l, r = _l, _r

    print(jobs_done)
    jobs_done = list(jobs_done)
    jobs_done.sort()
    arr = set(arr) - set(jobs_done)
    arr = list(arr)
    arr.sort()

print("arr", arr)
print(f"count :{counter}")
