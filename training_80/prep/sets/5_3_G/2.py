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
        env.add(tuple(map(int,row.split())))

    print(env)


    


    


   

if __name__ == '__main__':
    main()