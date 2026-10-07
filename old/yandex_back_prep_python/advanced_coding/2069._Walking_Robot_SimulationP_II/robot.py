from typing import List


class Robot:
    def __init__(self, heigth: int, width: int):
        self._heigth = heigth
        self._width = width

        self._direction = 0

        self._x_pos = 0
        self._y_pos = 0

        self._directions = {0: "East", 1: "South", 2: "West", 3: "North"}

    def _set_next_direction(self):
        if self._direction < len(self._directions) - 1:
            self._direction += 1
        else:
            self._direction = 0

    def step(self, num: int) -> None:
        while num > 0:
            match self._direction:
                case 0:
                    if self._x_pos + 1 < self._width:
                        self._x_pos += 1
                        num -= 1
                    else:
                        self._set_next_direction()
                        num -= 1
                case 1:
                    if self._y_pos + 1 < self._heigth:
                        self._y_pos += 1
                        num -= 1
                    else:
                        self._set_next_direction()
                        num -= 1
                case 2:
                    if self._x_pos - 1 > 0:
                        self._x_pos -= 1
                        num -= 1
                    else:
                        self._set_next_direction()
                        num -= 1
                case 3:
                    if self._y_pos - 1 > 0:
                        self._y_pos -= 1
                        num -= 1
                    else:
                        self._set_next_direction()
                        num -= 1

    def getPos(self) -> List[int]:
        return [self._x_pos, self._y_pos]

    def getDir(self) -> str:
        return self._directions[self._direction]
