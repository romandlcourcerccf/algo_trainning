import os


def is_five(row, col, table):
    rows = len(table)
    cols = len(table[0])
    # fmt: off
    if rows >=5 and cols >=5:
        if col <= cols - 5 and row <= rows - 5:
            if (table[row][col] == "X" or table[row][col] == "O") and table[row][col] == table[row][col + 1] == table[row][col + 2] == table[row][col + 3] == table[row][col + 4]:
                return True

            if (table[row][col] == "X" or table[row][col] == "O") and table[row][col] == table[row + 1][col] == table[row + 2][col] == table[row + 3][col] == table[row + 4][col]:
                return True

            if (table[row][col] == "X" or table[row][col] == "O") and table[row][col] == table[row + 1][col + 1] == table[row + 2][col + 2] == table[row + 3][col + 3] == table[row + 4][col + 4]:
                return True
        
            if (table[row][col + 4] == "X" or table[row][col + 4] == "O") and table[row][col + 4] == table[row +1][col + 3] == table[row + 2][col + 2] == table[row + 3][col + 1] == table[row + 4][col]:
                return True
        elif  col > cols - 5 and row <= rows - 5:
            if (table[row][col] == "X" or table[row][col] == "O") and table[row][col] == table[row][col + 1] == table[row][col + 2] == table[row][col + 3] == table[row][col + 4]:
                return True
        elif col <= cols - 5 and row > rows - 5:
             if (table[row][col] == "X" or table[row][col] == "O") and table[row][col] == table[row + 1][col] == table[row + 2][col] == table[row + 3][col] == table[row + 4][col]:
                return True
    elif rows < 5 and cols >=5:
        if col <= cols - 5:
            if (table[row][col] == "X" or table[row][col] == "O") and table[row][col] == table[row][col + 1] == table[row][col + 2] == table[row][col + 3] == table[row][col + 4]:
                return True
    elif rows >= 5 and cols < 5:
        if row <= rows - 5:
            if (table[row][col] == "X" or table[row][col] == "O") and table[row][col] == table[row + 1][col] == table[row + 2][col] == table[row + 3][col] == table[row + 4][col]:
                return True
    # fmt: on
    return False


def main():
    dname = os.path.dirname(__file__)

    # filename = os.path.join(dname, "input.txt")
    filename = os.path.join(dname, "1.txt")
    filename = os.path.join(dname, "2.txt")
    filename = os.path.join(dname, "5.txt")
    filename = os.path.join(dname, "6.txt")
    filename = os.path.join(dname, "7.txt")
    filename = os.path.join(dname, "8.txt")
    filename = os.path.join(dname, "9.txt")

    rows = open(filename, "r").readlines()[1:]
    rows = [r.rstrip() for r in rows]

    for r in rows:
        print(r)

    for row in range(len(rows)):
        for col in range(len(rows[0])):
            if is_five(row, col, rows):
                print("YES")
                return

    print("NO")
    return


if __name__ == "__main__":
    main()
