from atm import ATM


def test_deposit():
    atm = ATM()

    deposit = [40, 30, 20, 10, 5]

    atm.deposit(deposit)

    print(atm._cash)

    for i in range(len(atm._dinominations)):
        assert deposit[i] == atm._cash[atm._dinominations[i]]


def test_withdraw_1000():
    atm = ATM()

    deposit = [40, 30, 20, 10, 5]

    atm.deposit(deposit)

    res = atm.withdraw(1000)

    assert res[-1] == 2


def test_withdraw_1005():
    atm = ATM()

    deposit = [40, 30, 20, 10, 5]

    atm.deposit(deposit)

    res = atm.withdraw(1005)

    assert res == -1


def test_withdraw_800():
    atm = ATM()

    deposit = [40, 30, 20, 10, 5]

    atm.deposit(deposit)

    res = atm.withdraw(800)

    assert res == [0, 0, 1, 1, 1]
