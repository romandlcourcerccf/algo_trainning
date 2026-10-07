def main():

    with open("input.txt") as reader:
        matrix = reader.readlines()

    rows, cols = tuple(map(int, matrix[0].split()))

    matrix = matrix[1:]

    # print(f"cols {cols}, rows {rows}")
    # print(matrix)

    counter = 0
    for row in range(rows):
        for col in range(0, cols - 1):
            if matrix[row][col] == matrix[row][col + 1] == ".":
                counter += 1

    # print("counter :", counter)

    for col in range(cols):
        print(f"c: {col}")
        if rows == 2:
            if matrix[0][col] == matrix[1][col] == ".":
                counter += 1
        elif rows > 2:
            for row in range(0, rows - 1):
                if matrix[row][col] == matrix[row + 1][col] == ".":
                    counter += 1

    # print("counter :", counter)
    print(counter)


if __name__ == "__main__":
    main()
