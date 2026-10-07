import pytest
from solution_1 import Solution


@pytest.mark.parametrize(
    "lists, expected",
    [
        ([[1, 2], [3, 4, 5, 6]], [1, 3, 2, 4, 5, 6]),
    ],
)
def test_two_arrays(lists, expected):
    s = Solution(lists)

    for i in range(len(expected)):
        assert s.has_next()
        assert s.next() == expected[i]


@pytest.mark.parametrize(
    "lists, expected",
    [
        ([[1], [3, 4, 5, 6]], [1, 3, 4, 5, 6]),
    ],
)
def test_one_len_arrays(lists, expected):
    s = Solution(lists)

    for i in range(len(expected)):
        assert s.has_next()
        assert s.next() == expected[i]


@pytest.mark.parametrize(
    "lists, expected",
    [
        ([[1, 2], [3, 4], [5, 6]], [1, 3, 5, 2, 4, 6]),
    ],
)
def test_three_arrays(lists, expected):
    s = Solution(lists)

    for i in range(len(expected)):
        assert s.has_next()
        assert s.next() == expected[i]
