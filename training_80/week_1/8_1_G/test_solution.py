from solution import main
import os


def _read_from_file(file_name_prefix: str):
    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, file_name_prefix + ".txt")

    rows = open(filename, "r").readlines()
    rows = iter([r.rstrip() for r in rows])

    return rows


def test_solution_1(monkeypatch, capfd):
    rows = _read_from_file("1")

    monkeypatch.setattr("builtins.input", lambda _: next(rows))

    main()

    out, err = capfd.readouterr()
    assert out.rstrip() == "YES"


def test_solution_2(monkeypatch, capfd):
    rows = _read_from_file("2")

    monkeypatch.setattr("builtins.input", lambda _: next(rows))

    main()

    out, _ = capfd.readouterr()
    assert out.rstrip() == "YES"


# def test_solution_3(monkeypatch, capfd):
#     rows = _read_from_file("3")

#     monkeypatch.setattr("builtins.input", lambda _: next(rows))

#     main()

#     out, _ = capfd.readouterr()
#     assert out.rstrip() == "YES"


def test_solution_4(monkeypatch, capfd):
    rows = _read_from_file("4")

    monkeypatch.setattr("builtins.input", lambda _: next(rows))

    main()

    out, _ = capfd.readouterr()
    assert out.rstrip() == "YES"


def test_solution_5(monkeypatch, capfd):
    rows = _read_from_file("5")

    monkeypatch.setattr("builtins.input", lambda _: next(rows))

    main()

    out, _ = capfd.readouterr()
    assert out.rstrip() == "NO"


def test_solution_6(monkeypatch, capfd):
    rows = _read_from_file("6")

    monkeypatch.setattr("builtins.input", lambda _: next(rows))

    main()

    out, _ = capfd.readouterr()
    assert out.rstrip() == "YES"


def test_solution_7(monkeypatch, capfd):
    rows = _read_from_file("7")

    monkeypatch.setattr("builtins.input", lambda _: next(rows))

    main()

    out, _ = capfd.readouterr()
    assert out.rstrip() == "YES"


def test_solution_8(monkeypatch, capfd):
    rows = _read_from_file("8")

    monkeypatch.setattr("builtins.input", lambda _: next(rows))

    main()

    out, _ = capfd.readouterr()
    assert out.rstrip() == "NO"


def test_solution_9(monkeypatch, capfd):
    rows = _read_from_file("9")

    monkeypatch.setattr("builtins.input", lambda _: next(rows))

    main()

    out, _ = capfd.readouterr()
    assert out.rstrip() == "NO"
