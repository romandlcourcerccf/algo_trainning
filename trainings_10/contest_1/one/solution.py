def convert(var: str):
    stack = []
    for i, c in enumerate(var):
        if i == 0:
            stack.append(c.lower())
        else:
            if c.isupper():
                stack.append("_")
                stack.append(c.lower())
            else:
                stack.append(c.lower())

    return "".join(stack)


if __name__ == "__main__":
    lines = open("input.txt").readlines()[1:]

    for line in lines:
        print(convert(line.strip()))
