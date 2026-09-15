def solution():
    rows = open("3.txt").readlines()

    a_len, f_sum = tuple(map(int, rows[0].split()))
    arr = list(map(int, rows[1].split()))
    arr.sort()
    print(arr)

    l, r = 0, len(arr) - 1

    counter = 0
    while l < r:
        if arr[l] + arr[r] == f_sum:
            counter += 1
            l += 1
            r -= 1
        elif arr[l] + arr[r] < f_sum:
            l += 1
        elif arr[l] + arr[r] > f_sum:
            r -= 1

    print(counter)


if __name__ == "__main__":
    solution()

# 100
# 77 23 45 54 22
