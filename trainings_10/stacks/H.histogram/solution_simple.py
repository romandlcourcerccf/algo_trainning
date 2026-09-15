def solution(heights: list[int]):

    max_square = float("-inf")

    for idx in range(len(heights)):
        left = right = idx

        while left - 1 >= 0 and heights[left - 1] >= heights[idx]:
            left -= 1

        while right < len(heights) - 1 and heights[right + 1] >= heights[idx]:
            right += 1

        max_square = max(max_square, (right - left + 1) * heights[idx])

    print(max_square)


if __name__ == "__main__":
    heights = list(map(int, open("input.txt", "r").readlines()[0].split()[1:]))

    solution(heights)
