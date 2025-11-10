import pytest
from solution import MaxStack


@pytest.mark.parametrize(
    "commands, arguments, expected",
    [
        (
            [
                "push",
                "push",
                "push",
                "top",
                "popMax",
                "top",
                "peekMax",
                "pop",
                "top",
            ],
            [5, 1, 5, [], [], [], [], [], []],
            [None, None, None, 5, 5, 1, 5, 1, 5],
        ),
    ],
)
def test_one_edit_distance(commands, arguments, expected):
    ms = MaxStack()

    for idx, command in enumerate(commands):
        match command:
            case "push":
                assert ms.push(arguments[idx]) == expected[idx]
            case "pop":
                assert ms.pop() == expected[idx]
            case "top":
                assert ms.top() == expected[idx]
            case "peekMax":
                assert ms.peekMax() == expected[idx]
            case "popMax":
                assert ms.popMax() == expected[idx]
