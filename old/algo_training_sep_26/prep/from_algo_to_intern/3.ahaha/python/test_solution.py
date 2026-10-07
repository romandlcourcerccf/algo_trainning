from solution import Solution

import pytest


@pytest.mark.parametrize(
    "parameters, expected",
    [
        ("a", 1),
        ("s", 0),
        ("ahaha", 5),
        ("sdsdasdsds", 1),
        ("ahahsdsds", 4),
        ("sdsdahahahsdsds", 6),
    ],
)
def test_add_str_to_the_end(parameters, expected):
    s = Solution()

    res = s.get_solution(parameters)

    assert res == expected
