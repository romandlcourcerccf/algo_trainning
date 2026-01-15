import pytest
from solution import Solution


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 0, 1, 1, 0], 4),
        ([0, 1, 1, 1, 0], 4),
        ([0, 1, 1, 1, 0, 1, 1], 6),
        # ([1, 1, 1, 1, 1], 5),
        # ([0, 0, 0, 0, 0], 1),
    ],
)
def test_one_edit_distance(arr, expected):
    assert Solution().getMaxConsequteveOnesII(arr) == expected
