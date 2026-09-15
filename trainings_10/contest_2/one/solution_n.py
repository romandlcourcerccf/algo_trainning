def solution():
    rows = open("3.txt").readlines()

    a_len, f_sum = tuple(map(int, rows[0].split()))
    arr = list(map(int, rows[1].split()))
    stack = []
    counter = 0

    for v in arr:
        while stack and stack[-1] < v:
            stack.pop()

        if stack and stack[-1] + v == f_sum:
            counter += 1

        stack.append(v)

    print(counter)


if __name__ == "__main__":
    solution()

# 100
# 77 23 45 54 22
