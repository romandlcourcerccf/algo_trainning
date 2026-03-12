from collections import defaultdict, Counter


def main():

    _ = input("")
    word = input("")
    text = input("")

    # print(word)
    # print(text)

    w_counter = Counter(word)

    words_count = 0
    for i in range(len(text) - len(word) + 1):
        # print(text[i : i + len(word)])
        if Counter(text[i : i + len(word)]) == w_counter:
            words_count += 1

    print(words_count)


if __name__ == "__main__":
    main()
