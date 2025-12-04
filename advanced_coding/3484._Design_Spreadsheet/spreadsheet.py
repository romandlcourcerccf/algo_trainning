import string
from typing import Tuple


class SpreadsheetException(Exception):
    pass


class Spreadsheet:
    def __init__(self, rows: int):
        self._spreadsheet = []
        for _ in range(rows):  # TODO list compr
            self._spreadsheet.append([0] * 26)

        self._symbols_mapping = {}
        for idx, val in enumerate(string.ascii_uppercase[:26]):
            self._symbols_mapping[val] = idx

    def _get_cell_coordinates(self, sell: str) -> Tuple[int, int]:
        """
        Map mnemonic to coordinates : str -> col, row
            - The cell reference is provided in the format "AX" (e.g., "A1", "B10"),
        """
        return self._symbols_mapping[sell[0]], int(sell[1:])

    def setCell(self, sell: str, val: int) -> None:
        col, row = self._get_cell_coordinates(sell)

        print(f"sell: {sell} col: {col} row: {row}")

        if val > 105:
            raise SpreadsheetException(f"The val {val} above 105")

        self._spreadsheet[col][row] = val

    def resetCell(self, sell: str) -> None:
        col, row = self._get_cell_coordinates(sell)
        self._spreadsheet[col][row] = 0

    def _get_value(self, sell: str) -> int:
        col, row = self._get_cell_coordinates(sell)
        return self._spreadsheet[col][row]

    def getValue(self, formula: str) -> None:
        # TODO add req exp valid

        formula = formula.split("+")
        val1, val2 = formula[0][1:], formula[1]

        val1 = int(val1) if val1.isdigit() else self._get_value(val1)
        val2 = int(val2) if val2.isdigit() else self._get_value(val2)

        return val1 + val2
