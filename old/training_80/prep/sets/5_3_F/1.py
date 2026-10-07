import os

def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    # filename = os.path.join(dir_name, "1.txt")
    # filename = os.path.join(dir_name, "8.txt")
    # filename = os.path.join(dir_name, "3.txt")
    # filename = os.path.join(dir_name, "7.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]


    _dict = set(rows[0].split())
    corpus = list(rows[1].split())
    
    res = []
    for w in corpus:
        is_in_dict = False
        for i in range(len(w)):
            if w[:i] in _dict:
                res.append(w[:i])
                is_in_dict = True
                break
        
        if not is_in_dict:
            res.append(w)
    
    print(*res)

if __name__ == '__main__':
    main()