open_par = "("
close_par = ")"
operand = "1234567890"
operations = {"+": 0, "-": 0, "*": 1, "/": 1}


def to_invers(expr):
    ans = ""
    st = []

    for c in expr:
        if c in operand:
            ans = ans + c
        elif c == open_par:
            st.append(c)
        elif c in operations.keys():
            while len(st) > 0:
                _operation = st.pop()
                if (
                    _operation in operations.keys()
                    and operations[_operation] >= operations[c]
                ):
                    ans += _operation
                else:
                    st.append(_operation)
                    break
            st.append(c)

        elif c == close_par:
            while len(st) > 0:
                _operation = st.pop()
                if _operation in operations.keys():
                    ans += _operation
                elif _operation == open_par:
                    break

    while len(st) > 0:
        ans = ans + st.pop()

    print("what left :", st)

    return ans


def calc_inverce(expr):
    s = []

    for e in expr:
        if e == "+":
            op1 = s.pop()
            op2 = s.pop()
            s.append(int(op1) + int(op2))
        elif e == "*":
            op1 = s.pop()
            op2 = s.pop()
            s.append(int(op1) * int(op2))
        else:
            s.append(e)

    return s


if __name__ == "__main__":
    test1 = {"in": "6+7", "out": "67+"}
    test2 = {"in": "(6+7)", "out": "67+"}
    test3 = {"in": "(6+7)*2", "out": "67+2*"}
    test4 = {"in": "6+3*(1+4+5)*2", "out": "63145*+*2*+"}

    tests = [test1, test2, test3, test4]

    # expr = '6+3*(1+4+5)*2'
    # expected = '63145*+*2*+'
    # answer = to_invers(expr)

    # print('expected :', expected)
    # print('answer   :', answer)

    # assert expected == answer

    # print(to_invers(expr))

    for test in tests:
        out = to_invers(test["in"])
        print("in: ", test["in"], "out: ", out, "exp: ", test["out"])

    print(calc_inverce("67+2*"))
