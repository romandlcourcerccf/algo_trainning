from solution import main
import sys
import os


def _read_from_file(file_name_prefix: str):
    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, file_name_prefix + ".txt")

    rows = open(filename, "r").readlines()
    rows = iter([r.rstrip() for r in rows])

    return rows


def _get_test_num(method_name: str) -> int:
    return method_name.split("_")[2]


def test_solution_1(monkeypatch, capfd):
    test_num = _get_test_num(sys._getframe().f_code.co_name)
    rows = _read_from_file(test_num)

    monkeypatch.setattr("builtins.input", lambda _: next(rows))

    main()

    # out, err = capfd.readouterr()
    # assert out.rstrip() == "0"
