from spreadsheet import Spreadsheet, SpreadsheetException
import pytest


def test_set_cell():
    spreadsheet = Spreadsheet(rows=3)
    spreadsheet.setCell("A1", 10)
    assert spreadsheet._get_value("A1") == 10


def test_set_sell_wrong_value():
    spreadsheet = Spreadsheet(rows=3)
    with pytest.raises(SpreadsheetException):
        spreadsheet.setCell("A1", 200)

    assert spreadsheet._get_value("A1") == 0


def test_reset_cell():
    spreadsheet = Spreadsheet(rows=3)
    spreadsheet.setCell("C2", 10)
    spreadsheet.resetCell("C2")
    assert spreadsheet._get_value("C2") == 0


@pytest.mark.parametrize(
    "cell1,cell1_val,cell2,cell2_val,formula,expected",
    [
        (["A1", 10, "A2", 10, "=A1+A2", 20]),
        (["A1", 10, "A1", 10, "=A1+A1", 20]),
        (["A1", 10, "A1", 10, "=6+A1", 16]),
    ],
)
def test_get_value(cell1, cell1_val, cell2, cell2_val, formula, expected):
    spreadsheet = Spreadsheet(rows=10)

    spreadsheet.setCell(cell1, cell1_val)
    spreadsheet.setCell(cell2, cell2_val)

    assert spreadsheet.getValue(formula) == expected
