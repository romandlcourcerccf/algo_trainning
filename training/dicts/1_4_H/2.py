import os
from collections import defaultdict, Counter
def main():

    dir_name = os.path.dirname(__file__)
    # filename = os.path.join(dir_name, "2.txt")
    filename = os.path.join(dir_name, "input.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]


    word = list(rows[1])
    sentence = list(rows[2])

 
    word_dict =  Counter(word)
    pattern_dict = defaultdict(int)

    hit_count = 0
   
    for i in range(0, len(sentence) - len(word)+1):
        if i == 0:
            for _i in range(i, len(word)):
                pattern_dict[sentence[_i]] +=1 

        else:

            # print('sentence[i-1] ', sentence[i-1]) 
            # print('sentence[i + len(word)] ', sentence[i + len(word)-1]) 

            pattern_dict[sentence[i-1]] -=1

            if pattern_dict[sentence[i-1]] == 0:
                del pattern_dict[sentence[i-1]]

            pattern_dict[sentence[i + len(word)-1]] +=1

        # print('i :', i)
        # print('word_dict     :', word_dict)
        # print('pattern_dict :', pattern_dict)

        if word_dict == pattern_dict:
            hit_count +=1

    print(hit_count)



if __name__ == '__main__':
    main()
