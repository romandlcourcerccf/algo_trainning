from collections import defaultdict

def main():

    ansestry_tree = defaultdict(set)

    persons = set()
    rows_count = int(input(""))

    for _ in range(rows_count - 1):
        row = input("").split()
        ansestry_tree[row[1]].add(row[0])
        persons.add(row[0])
        persons.add(row[1])

    persons = sorted(list(persons))

    for person in persons:
        l = []
        decscendents = set()

        cur = person
        l.append(cur)

        while l:
            v = l.pop()
            decscendents.add(v)
            for d in ansestry_tree[v]:
                l.append(d)

        print(person, "", len(decscendents) - 1)


if __name__ == "__main__":
    main()
