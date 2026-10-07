import os
from collections import defaultdict
from random import randrange


class TestDataIterator:
    def __init__(
        self,
        min_parts_num: int,
        min_part_len: int,
        max_parts_num: int,
        max_part_len: int,
        ex_num: int,
    ):
        self.min_parts_num = min_parts_num
        self.min_part_len = min_part_len
        self.max_parts_num = max_parts_num
        self.max_part_len = max_part_len
        self.ex_num = ex_num

    def _gen_data(self):
        sequence = []

        for _ in range(self.ex_num):
            part_len = randrange(self.min_part_len, self.max_part_len)
            parts_num = randrange(self.min_parts_num, self.min_parts_num)

            sequence.append(
                [randrange(self.max_val) for i in range(randrange(2, self.max_len))]
            )

        return sequence

    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

    def __iter__(self):
        return self


def main():
    dname = os.path.dirname(__file__)

    filename = os.path.join(dname, "input.txt")
    filename = os.path.join(dname, "1.txt")
    filename = os.path.join(dname, "2.txt")
    filename = os.path.join(dname, "3.txt")
    # filename = os.path.join(dname, "13.txt")

    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]

    full_string = rows[1]

    parts = [r for r in rows[2:]]

    parts_nums = defaultdict(int)

    for i in range(len(rows[2:])):
        parts_nums[rows[2:][i]] = i + 1

    for part, idx in enumerate(range(len(rows[2:]))):
        parts_nums[part] = idx + 1

    part_len = len(parts[0])

    h = defaultdict(list)

    for i in range(0, len(full_string) - part_len + 1):
        h[full_string[i : i + part_len]].append(i)

    print(h)

    res = []
    for part in parts:
        if part in h:
            res.append((h[part].pop(), parts_nums[part]))

    print(res)
    res.sort()

    res = [r[1] for r in res]

    print(*res)


if __name__ == "__main__":
    main()
