from collections import defaultdict, Counter
import string


def main():

    words_dict = defaultdict(set)
    dict_size = int(input(""))
    upper_case_letters = set([c for c in string.ascii_uppercase])

    for _ in range(dict_size):
        word = input("")
        words_dict[word].add(word)

    sentence = input("").split()

    # print(words_dict)
    # print(sentence)

    good_words = []
    bad_words = []

    # Вася решил, что в словах, которых нет в словаре, он будет считать, что Петя поставил ударения правильно,
    # если в этом слове Петей поставлено ровно одно ударение.
    # Оказалось, что в некоторых словах ударение может быть поставлено больше, чем одним способом.
    # Вася решил, что в этом случае если то, как Петя поставил ударение, соответствует одному из приведённых в словаре вариантов,
    # он будет засчитывать это как правильную расстановку ударения, а если не соответствует, то как ошибку.

    for word in sentence:
        if word not in words_dict:
            if (
                set([c for c in word]) & upper_case_letters
                and len(set([c for c in word]) & upper_case_letters) == 1
            ):
                good_words.append(word)
            else:
                bad_words.append(word)
        elif word in words_dict:
            good_words.append(word)

        # if word not in words_dict and not set([c for c in word]) & upper_case_letters:
        #     errors_count += 1

    print("good_words :", good_words, " :", len(good_words))
    print("bad_words :", bad_words, " :", len(bad_words))
    print("##########")


if __name__ == "__main__":
    main()
