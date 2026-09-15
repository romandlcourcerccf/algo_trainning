def solution(heights: list[int]):

    area = 0
    stack = [0]

    heights = [0] + heights + [0]

    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            area = max(area, heights[stack.pop()] * (i - stack[-1] - 1))

        stack.append(i)

    print(area)


if __name__ == "__main__":
    heights = list(map(int, open("input.txt", "r").readlines()[0].split()[1:]))

    solution(heights)
