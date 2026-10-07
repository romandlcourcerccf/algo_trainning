import os


def main():


    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, "3.txt")
    filename = os.path.join(dname, "input.txt")

    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip().split() for r in rows]


    rows = [list(map(int, r)) for r in rows]


    N = list(map(int, rows[1]))
    K = list(map(int, rows[2]))

    N.sort()
    
    def bin_search(arr, n):

        l,r = 0, len(arr)

        while l < r:

            m = (l+r) // 2
            if n == arr[m]:
                return True
            elif n < arr[m]:
                r = m
            else:
                l = m+1

        return False

    for k in K:
        print('YES' if bin_search(N, k) else 'NO')


if __name__ == "__main__":
    main()
