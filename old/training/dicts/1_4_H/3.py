import os
from collections import defaultdict, Counter
def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "1.txt")
    # filename = os.path.join(dir_name, "input.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]


    word = list(rows[1])
    sentence = list(rows[2])

 
    word_dict =  Counter(word)
    pattern_dict = defaultdict(int)

    hit_count = 0
    eq_count=0 
    for i in range(0, len(sentence) - len(word)+1):
        if i == 0:
            for _i in range(i, len(word)):
                pattern_dict[sentence[_i]] +=1 

            for k in pattern_dict.keys():
                if k in word_dict and word_dict[k] == pattern_dict[k]:
                    eq_count +=1

            if word_dict == pattern_dict:
                hit_count +=1

        else:

            prev_hit = 0
            if sentence[i-1] in pattern_dict and sentence[i-1] in word_dict and pattern_dict[sentence[i-1]] == word_dict[sentence[i-1]]:
                prev_hit +=1
            
            next_hit = 0
            if sentence[i + len(word)-1] in pattern_dict and sentence[i + len(word)-1] in word_dict and pattern_dict[sentence[i + len(word)-1]] == word_dict[sentence[i + len(word)-1]]:
                next_hit +=1

            pattern_dict[sentence[i-1]] -=1

            if pattern_dict[sentence[i-1]] == 0:
                del pattern_dict[sentence[i-1]]
            
            if sentence[i-1] in pattern_dict and sentence[i-1] in word_dict and pattern_dict[sentence[i-1]] == word_dict[sentence[i-1]]:
                eq_count +=1

            pattern_dict[sentence[i + len(word)-1]] +=1

            if sentence[i + len(word)-1] in pattern_dict and sentence[i + len(word)-1] in word_dict and pattern_dict[sentence[i + len(word)-1]] == word_dict[sentence[i + len(word)-1]]:
                eq_count +=1
            


        # print('i :', i)
        # print('word_dict     :', word_dict)
        # print('pattern_dict :', pattern_dict)

        if eq_count == len(word):
            hit_count +=1

    print(hit_count)



if __name__ == '__main__':
    main()
