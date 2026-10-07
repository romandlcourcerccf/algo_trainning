from collections import defaultdict


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    banking_system = defaultdict(int)

    with open("input.txt", "r") as reader:
        transactions = reader.readlines()

    for transaction in transactions:
        transaction = transaction.split()
        command = transaction[0]
        match command:
            case "DEPOSIT":
                banking_system[transaction[1]] += int(transaction[2])
            case "WITHDRAW":
                banking_system[transaction[1]] -= int(transaction[2])
            case "TRANSFER":
                # print("-->", banking_system)
                client1 = transaction[1]
                client2 = transaction[2]
                amount = int(transaction[3])

                # print(f" client1 :{client1} client2 :{client2} amount: {amount}")

                if client1 not in banking_system:
                    banking_system[client1] = 0
                if client2 not in banking_system:
                    banking_system[client2] = 0

                banking_system[client1] -= amount
                banking_system[client2] += amount
                # print(banking_system)

            case "INCOME":
                income = int(transaction[1])

                for client in banking_system:
                    if banking_system[client] > 0:
                        banking_system[client] += int(
                            banking_system[client] * (income / 100)
                        )

            case "BALANCE":
                name = transaction[1]
                if name in banking_system:
                    print(banking_system[name])
                else:
                    print("ERROR")


if __name__ == "__main__":
    main()
