def solution():
    _ = input()
    cities = input().split()
    cities = list(map(int, cities))

    res = [-1] * len(cities)
    stack = []

    for i, v in enumerate(cities):
        while stack and stack[-1][1] > v:
            res[stack[-1][0]] = i
            stack.pop()

        stack.append((i, v))

    print(*res)


if __name__ == "__main__":
    solution()
