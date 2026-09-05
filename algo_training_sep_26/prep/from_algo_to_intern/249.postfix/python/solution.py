def solution(expr: str) -> int:

    operatios = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    st = []

    expr = expr.split()

    for op in expr:
        if op in operatios.keys():
            op1 = st.pop()
            op2 = st.pop()
            st.append(operatios[op](op2, op1))

        else:
            st.append(int(op))

    return st[0]


if __name__ == "__main__":
    lines = open("input.txt").readlines()
    print(solution(lines[0]))
