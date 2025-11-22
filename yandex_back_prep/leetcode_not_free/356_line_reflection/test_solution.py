import pytest
from _solution import Solution


@pytest.mark.parametrize(
    "points, expected",
    [
        ([[-1, 1], [0, 0]], False),
        ([[-1, 1], [0, 0]], False),
        ([[-1, 1], [0, 0], [200, 300]], False),
        ([[1, 1], [1, 0]], True),
        ([[1, 1], [1, 0]], True),
        ([[1, 1], [1, 0], [2, 1], [2, 0]], True),
        ([[1, 1]], True),
    ],
)
def test_solution(points, expected):
    assert Solution().line_reflection(points) == expected
