from typing import List


class SQL:
    def __init__(self, names: str, columns: List[int]) -> None:
        self.tables = {}

        self.names = names
        self.columns = columns

    def insertRow(self, name: str, row: List[str]) -> None:
        if name not in self.tables:
            self.tables[name] = {}

        table = self.tables[name]
        table_ln = len(table)
        table[table_ln + 1] = row.copy()

    def deleteRow(self, name: str, rowId: int) -> None:
        table = self.tables[name]
        if rowId in table:
            del table[rowId]

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        table = self.tables[name]

        return table[rowId][columnId]
