import sys
import heapq


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    lines = open("2.txt", "r").readlines()

    N = int(lines[0])
    groups = list(map(int, lines[1].split()))

    locker_room = []
    cur_group = 0

    max_locker_room_size = float("-inf")

    for g in groups:
        heapq.heappush(locker_room, g)

        if heapq.nsmallest(1, locker_room)[0] == cur_group + 1:
            heapq.heappop(locker_room)
            cur_group += 1

        max_locker_room_size = max(max_locker_room_size, len(locker_room))

    print(max_locker_room_size)


if __name__ == "__main__":
    main()
