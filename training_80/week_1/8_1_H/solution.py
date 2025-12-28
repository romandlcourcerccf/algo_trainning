from collections import defaultdict


def main():
    str_len, chank_num = tuple(map(int, input("").split()))
    chank_len = int(str_len / chank_num)

    # print("str_len :", str_len)
    # print("chank_num :", chank_num)
    # print("chank_len :", chank_len)

    string = input("")

    # string = string.rstrip()
    # print("string :", string)

    h = defaultdict(list)

    count = 1
    for i in range(0, str_len, chank_len):
        h[string[i : i + chank_len]].append(count)
        count += 1

    order = []
    for i in range(chank_num):
        chank = input("")
        # print(f"{i + 1} >>> chank: ", chank)
        pos = h[chank].pop()
        order.append((pos, i + 1))

    order.sort()
    order = [o[1] for o in order]

    print(*order)
