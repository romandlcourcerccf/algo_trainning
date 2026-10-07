import os

def main():

    dir_name = os.path.dirname(__file__)
    # filename = os.path.join(dir_name, "input.txt")
    filename = os.path.join(dir_name, "1.txt")
    # filename = os.path.join(dir_name, "8.txt")
    # filename = os.path.join(dir_name, "3.txt")
    # filename = os.path.join(dir_name, "7.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]


    print(rows)

    env = set()

    for row in rows[1:]:
        row = tuple(map(int,row.split()))
        env.add(row)

    print(env)

    res = []

    for p1 in list(env):
        for p2 in list(env):
            if p1 != p2:
                x1, y1 = p1
                x2, y2 = p2
                if x1 == x2:
                    print('x1 == x2 x1 :{x1} x2: {x2}')
                    delta = abs(y1, y2)
                    if (x1+delta, y1) in env and (x2+delta, y2) in env:
                        res.append((x1+delta, y1))
                        res.append((x2+delta, y2))
                        print(res)
                        return
                    elif (x1-delta, y1) in env and (x2-delta, y2) in env:
                        res.append((x1-delta, y1))
                        res.append((x2-delta, y2))
                        print(res)
                        return

                elif y1 == y2:
                    print('y1 == y2 y1 :{y1} y2: {y2}')
                    delta = abs(x1, x2)
                    if (x1, y1+delta) in env and (x2, y2+delta) in env:
                        res.append((x1, y1+delta))
                        res.append((x2, y2+delta))
                        print(res)
                        return
                    elif (x1, y1-delta) in env and (x2, y2-delta) in env:
                        res.append((x1, y1-delta))
                        res.append((x2, y2-delta))
                        print(res)
                        return
                else:
                    print(f'y1 != y2 y1 :{y1} y2: {y2}')
                    print(f'p1 {p1} p2 {p2}')
                    dx = abs(x1 - x2)
                    dy = abs(y1 - y2)

                    if (x1+dx, y1+dy) in env and (x2+dx, y2+dy) in env:
                        res.append((x1+dx, y1+dy))
                        res.append((x2+dx, y2+dy))
                        print(res)
                        
                    elif (x1-dx, y1-dy) in env and (x2-dx, y2-dy) in env:
                        res.append((x1-dx, y1-dy))
                        res.append((x2-dx, y2-dy))
                        print(res)
                        

if __name__ == '__main__':
    main()