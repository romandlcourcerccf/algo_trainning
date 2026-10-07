from collections import defaultdict


def main():

    ansestry_tree = defaultdict(set)
    calculated_decsendants = defaultdict(set)

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
                if d in calculated_decsendants:
                    decscendents = decscendents | calculated_decsendants[d]
                else:
                    l.append(d)

        calculated_decsendants[person] = decscendents

    for person in sorted(list(calculated_decsendants.keys())):
        print(f"{person} {len(calculated_decsendants[person]) - 1}")


if __name__ == "__main__":
    main()
