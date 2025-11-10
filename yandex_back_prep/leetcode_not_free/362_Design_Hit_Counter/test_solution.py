import pytest
from solution import HitCounter


@pytest.mark.parametrize(
    "commands, arguments, expected",
    [
        (
            ["hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"],
            [1, 2, 3, 4, 300, 300, 301],
            [None, None, None, 3, None, 4, 3],
        ),
        (
            ["hit", "hit", "hit", "hit"],
            [1, 2, 3, 20],
            [None, None, None, None],
        ),
    ],
)
def test_hits_counter(commands, arguments, expected):
    print("commands :", commands)
    print("arguments :", arguments)
    print("expected :", expected)

    hc = HitCounter()

    for idx, command in enumerate(commands):
        match command:
            case "hit":
                assert hc.hit(arguments[idx]) == expected[idx]
            case "getHits":
                assert hc.getHits(arguments[idx]) == expected[idx]
