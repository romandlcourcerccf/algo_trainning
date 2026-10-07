import os

dir_name = os.path.dirname(__file__)
file = os.path.join(dir_name, "input.txt")
# file = os.path.join(dir_name, '3.txt')
file = os.path.join(dir_name, "4.txt")

with open(file, "r") as reader:
    rows = reader.readlines()
    rows = [r.rstrip() for r in rows]

s = []


for row in rows:
    row = row.split(" ")
    if len(row) == 1:
        match row[0]:
            case "pop":
                if s:
                    print(s.pop())
                else:
                    print("error")
            case "back":
                if s:
                    print(s[-1])
                else:
                    print("error")
            case "size":
                print(len(s))
            case "clear":
                s.clear()
                print("ok")
            case "exit":
                print("bye")
                break
    elif len(row) == 2:
        match row[0]:
            case "push":
                s.append(row[1])
                print("ok")
