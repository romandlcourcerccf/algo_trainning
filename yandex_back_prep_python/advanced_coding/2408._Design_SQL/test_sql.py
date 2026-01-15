from sql import SQL

import pytest

# Input
# ["SQL", "insertRow", "selectCell", "insertRow", "deleteRow", "selectCell"]
# [[["one", "two", "three"], [2, 3, 1]], ["two", ["first", "second", "third"]], ["two", 1, 3], ["two", ["fourth", "fifth", "sixth"]], ["two", 1], ["two", 2, 2]]
# Output
# [null, null, "third", null, null, "fifth"]

# @pytest.mark.parametrize(
#     "cell1,cell1_val,cell2,cell2_val,formula,expected",
#     [
#         (["A1", 10, "A2", 10, "=A1+A2", 20]),
#         (["A1", 10, "A1", 10, "=A1+A1", 20]),
#         (["A1", 10, "A1", 10, "=6+A1", 16]),
#     ],
# )


# @pytest.mark.parametrize(
# )


def test_sql():
    sql = SQL("cats, dogs, racoons", [1, 2, 3])

    sql.insertRow("cats", ["Tom"])
    sql.insertRow("cats", ["Ginger"])

    sql.insertRow("dogs", ["Tom", "Black"])
    sql.insertRow("dogs", ["Ginger", "White"])

    sql.insertRow("racoons", ["Kinky", "Black", "Thin"])
    sql.insertRow("racoons", ["Stinky", "White", "Obies"])

    assert sql.selectCell("racoons", 1, 0) == "Kinky"
    assert sql.selectCell("racoons", 2, 1) == "White"

    sql.deleteRow("dogs", 1)
