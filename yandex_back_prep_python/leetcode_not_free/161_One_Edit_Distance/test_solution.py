import pytest
from solution import Solution


@pytest.mark.parametrize(
    "s, t, expected",
    [("ab", "abc", True), ("", "", False), ("abc", "ab", True), ("bobo", "boba", True)],
)
def test_one_edit_distance(s, t, expected):
    assert Solution().isOneEditDistance(s, t) is expected
