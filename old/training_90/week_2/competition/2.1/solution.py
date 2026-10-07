import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """

    # with open("input.txt", "r") as reader:
    #     rows = reader.readlines()
    #     rows = [r.strip() for r in rows]

    # message = rows[1]
    # print("message :", message)

    _ = input("")
    message = input("")

    max_len = float("-inf")

    cur_len = 0
    cur_char = ""
    for c in message:
        # print(f"max_len : {max_len} cur_len : {cur_len} cur_char {cur_char}")
        if c != "a" and c != "h":
            max_len = max(max_len, cur_len)
            cur_len = 0
            cur_char = ""
        elif c == "a":
            if cur_len == 0:
                cur_len += 1
                cur_char = c
            elif cur_len > 0:
                if cur_char != "h":
                    max_len = max(max_len, cur_len)
                    cur_len = 1
                    cur_char = c
                else:
                    cur_len += 1
                    cur_char = c

        elif c == "h":
            if cur_len == 0:
                cur_len += 1
                cur_char = c
            elif cur_len > 0:
                if cur_char != "a":
                    max_len = max(max_len, cur_len)
                    cur_len = 1
                    cur_char = c
                else:
                    cur_len += 1
                    cur_char = c

        max_len = max(max_len, cur_len)

    print(max_len)


if __name__ == "__main__":
    main()
