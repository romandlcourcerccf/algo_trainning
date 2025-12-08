from cal import Calendar

import pytest

# Input
# ["MyCalendar", "book", "book", "book"]
# [[], [10, 20], [15, 25], [20, 30]]
# Output
# [null, true, false, true]


@pytest.mark.parametrize(
    "intervals, expected",
    [
        ([[10, 20], [15, 25], [20, 30]], [True, False, True]),
    ],
)
def test_calendar(intervals, expected):
    calendar = Calendar()

    for i in range(len(intervals)):
        calendar.book(intervals[i][0], intervals[i][1]) == expected[i]
