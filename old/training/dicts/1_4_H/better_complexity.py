import os
from collections import defaultdict, Counter

def get_similarity(dict_1, dict_2):
    similarity = 0
    for c in dict_1:
        if c in dict_2 and dict_1[c] == dict_2[c]:
            similarity +=1
    return similarity

def modify_dict(s_dict, w_dict, symbol, modifier):
    res = 0
    if symbol not in s_dict:
        s_dict[symbol] = 0

    if symbol in w_dict and s_dict[symbol] == w_dict[symbol]:
        res = -1

    s_dict[symbol] += modifier

    if symbol in w_dict and s_dict[symbol] == w_dict[symbol]:
        res  = 1
    
    return res

def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "1.txt")
    # filename = os.path.join(dir_name, "input.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

   
    len_word, len_phrase = list(map(int, rows[0].split()))

    hit_counter = 0

    word = list(rows[1])
    phrase = list(rows[2])

    word_dict = Counter(word)
    phrase_dict = Counter(phrase[:len_word])

    similarity = get_similarity(word_dict, phrase_dict)

    if similarity == len(word_dict):
        hit_counter +=1

    for i in range(len_word, len_phrase):

        similarity += modify_dict(word_dict, phrase_dict, phrase[i-len_word], -1)
        similarity += modify_dict(word_dict, phrase_dict, phrase[i], +1)

        if similarity == len(word_dict):
            hit_counter +=1

    print(hit_counter)

if __name__ == '__main__':
    main()
