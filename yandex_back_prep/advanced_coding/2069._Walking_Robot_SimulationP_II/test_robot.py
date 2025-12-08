from robot import Robot
import pytest


@pytest.mark.parametrize(
    "height, width, step, direction, position",
    [
        (5, 5, 2, "East", [2, 0]),
        (5, 5, 6, "South", [4, 1]),
    ],
)
def test_step(height, width, step, direction, position):
    robot = Robot(height, width)

    robot.step(step)

    assert robot.getDir() == direction
    assert robot.getPos() == position
