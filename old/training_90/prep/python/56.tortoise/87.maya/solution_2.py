from collections import Counter


def main():

    _ = input("")
    word = input("")
    text = input("")

    lt = len(text)
    lw = len(word)

    w_counter = Counter(word)

    words_count = 0
    s_counter = Counter(text[0:lw])

    for i in range(1, lt - lw + 1):
        if s_counter == w_counter:
            words_count += 1

        s_counter[text[i - 1]] -= 1
        if s_counter[text[i - 1]] == 0:
            del s_counter[text[i - 1]]

        s_counter[text[i + lw - 1]] += 1

    if s_counter == w_counter:
        words_count += 1

    print(words_count)


if __name__ == "__main__":
    main()
