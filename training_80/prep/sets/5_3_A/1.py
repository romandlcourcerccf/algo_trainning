import os

def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    # filename = os.path.join(dir_name, "1.txt")
    # filename = os.path.join(dir_name, "2.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]


    _set = None
    for i in range(len(rows)): 
        if i % 2 == 0 and i > 0:
            if not _set:
                _set = set()
                _set.update(rows[i].split())
            else:
                __set = set()
                __set.update(rows[i].split())

                _set = _set & __set

    print(len(_set))
    print(*sorted(list(_set)))

    
if __name__ == '__main__':
    main()