import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """

    stack = []

<<<<<<< HEAD
    row = input()
=======
    row = input("")
>>>>>>> 9c6a377a9cb9661be124a2a1b9c7eaaeeccd1f98
    while row != "exit":
        sp = row.split()
        if len(sp) == 1:
            sp = sp[0]
            match sp:
                case "size":
                    print(len(stack))
                case "back":
                    if len(stack) > 0:
                        print(stack[-1])
                    else:
                        print("error")
                case "pop":
                    if len(stack) > 0:
                        print(stack[-1])
                        stack.pop()
                    else:
                        print("error")
                case "clear":
                    stack.clear()
                    print("ok")
                case "exit":
                    print("bye")
                    return

        elif len(sp) == 2:
            cmd, op = sp
            match cmd:
                case "push":
                    stack.append(int(op))
                    print("ok")

<<<<<<< HEAD
        row = input()
=======
        row = input("")
>>>>>>> 9c6a377a9cb9661be124a2a1b9c7eaaeeccd1f98

    print("bye")


if __name__ == "__main__":
    main()
