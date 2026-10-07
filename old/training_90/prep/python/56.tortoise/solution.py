from collections import defaultdict, deque


def is_tall_true():
    pass


def main():

    totrtoises_number = int(input(""))
    tortoises = []
    for _ in range(totrtoises_number):
        tortoises.append(list(map(int, input("").split())))

    for i, t in enumerate(tortoises):
        print("i :", i, "t :", t)

    print(tortoises)


if __name__ == "__main__":
    main()
