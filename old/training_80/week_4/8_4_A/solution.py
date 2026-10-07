from typing import List


def str_to_seconds(_str: str) -> int:
    _time = _str.split(":")
    return int(_time[0]) * 60 + int(_time[1])


def fill_time_line(
    time_line: List[int], vouages: List[str], direction: str
) -> List[int]:
    for out_vouage_interval in vouages:
        vouage_interval = out_vouage_interval.split("-")

        start_time = str_to_seconds(vouage_interval[0])
        end_time = str_to_seconds(vouage_interval[1])

        time_line.append((start_time, "start", direction))
        time_line.append((end_time, "end", direction))


def main():
    out_vouages_count = int(input(""))
    out_vouages_intervals = []

    for _ in range(out_vouages_count):
        out_vouages_intervals.append(input(""))

    in_vouages_count = int(input(""))
    in_vouages_intervals = []

    for _ in range(in_vouages_count):
        in_vouages_intervals.append(input(""))

    time_line = []

    fill_time_line(time_line, out_vouages_intervals, "out")
    fill_time_line(time_line, in_vouages_intervals, "in")

    time_line.sort()

    cars_start = 0
    cars_end = 0

    min_cars_start = float("inf")
    min_cars_end = float("inf")

    for time in time_line:
        if time[1] == "start" and time[2] == "out":
            cars_start -= 1

        if time[1] == "end" and time[2] == "out":
            cars_end += 1

        if time[1] == "start" and time[2] == "in":
            cars_end -= 1

        if time[1] == "end" and time[2] == "in":
            cars_start += 1

        min_cars_start = min(min_cars_start, cars_start)
        min_cars_end = min(min_cars_end, cars_end)

    print(abs(min_cars_start) + abs(min_cars_end))


if __name__ == "__main__":
    main()
