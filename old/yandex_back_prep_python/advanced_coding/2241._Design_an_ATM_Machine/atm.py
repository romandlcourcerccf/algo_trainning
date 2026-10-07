from typing import List


class ATM:
    def __init__(self):
        self._dinominations = [20, 50, 100, 200, 500]
        self._cash = {}
        for dinomenation in self._dinominations:
            self._cash[dinomenation] = 0

    def deposit(self, bancnotes_count: List[int]) -> None:
        for idx, denomination in enumerate(self._dinominations):
            self._cash[denomination] += bancnotes_count[idx]

    def withdraw(self, amount: int) -> int:
        res = [0] * len(self._dinominations)
        _amount = amount

        print(f"Widthraw {amount}")
        for i in range(len(self._dinominations) - 1, -1, -1):
            print(f"amount : {_amount}")
            if _amount == 0:
                break

            if _amount < self._dinominations[i]:
                return -1

            print(
                f"dn {self._dinominations[i]} amount {_amount}  total {self._cash[self._dinominations[i]] * self._dinominations[i]} "
            )
            total_denom = self._cash[self._dinominations[i]] * self._dinominations[i]
            bancnotes_count = _amount // self._dinominations[i]
            to_withdraw = bancnotes_count * self._dinominations[i]
            print(f" >> bancnotes_count  {bancnotes_count}")

            if to_withdraw <= total_denom:
                res[i] = bancnotes_count
                _amount -= to_withdraw

            else:
                return -1

        for i in range(len(res)):
            self._cash[self._dinominations[i]] -= res[i]

        return res
