from collections import defaultdict


def solution():
    result = []
    rows = open("1.txt").readlines()
    arr = rows[0]
    stack = []
    h = defaultdict(int)

    for _, c in enumerate(arr):
        if c not in ["<", ">", "/"]:
            stack.append(c)

        h[c] += 1

    print(stack)
    print(h)

    for c in set(stack):
        if h[c] % 2 != 0:
            print("Impossible")
            return

    if h["<"] != h[">"]:
        print("Impossible")
        return

    if (h["<"] + h["<"]) / 4 != h["/"]:
        print("Impossible")
        return

    stack = set(stack)

    for i in range(h["<"]):
        el = ""
        el += "<"
        el_content = ""
        if i != h["<"] - 1:
            el_content += stack.pop()
        else:
            while stack:
                el_content += stack.pop()

        el += el_content
        el += ">"

        result.insert(0, el)

        el = ""
        el += "<"
        el += "</"

        el_content = ""
        if i != h["<"] - 1:
            el_content += stack.pop()
        else:
            while stack:
                el_content += stack.pop()

        el += el_content
        el += ">"

        result.append(el)

    print("".join(result))


if __name__ == "__main__":
    solution()


# <>test<>//<>test<>

# <
# >
# /


# <e><stt></stt></e>
