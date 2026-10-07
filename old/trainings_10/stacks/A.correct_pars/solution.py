def _solution():
    seq = input()
    open = ["(", "[", "{"]
    pairs = ["()", "[]", "{}"]
    st = []
    for c in seq:
        if c in open:
            st.append(c)
        else:
            if not st:
                print("no")
                return
            _c = st.pop()
            if _c + c not in pairs:
                print("no")
                return

    print("yes") if not st else print("no")


if __name__ == "__main__":
    _solution()
