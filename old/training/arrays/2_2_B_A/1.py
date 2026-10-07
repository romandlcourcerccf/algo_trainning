import os

def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    # filename = os.path.join(dir_name, "1.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    # print(rows)

    rows = list(map(int, rows))

    _max = max(rows)

    res = 0

    for n in rows:
        if n == _max:
            res +=1

    print(res)

if __name__ == '__main__':
    main()