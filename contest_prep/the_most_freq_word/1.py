import sys
from collections import defaultdict

def main():
    
    rows = sys.stdin.readlines()

    # with open('/Users/roman/projects/algo_trainning/contest_prep/the_most_freq_word/2.txt', 'r') as f:
    #     rows = f.readlines()

    h = defaultdict(int)

    for row in rows:
        words = row.split()
        for w in words:
            h[w] +=1
    
    # print(h)

    max_word_num = max(h.values())

    # print(max_word_num)

    max_words = []

    for k,v in h.items():
        if v == max_word_num:
            max_words.append(k)

    max_words.sort()

    print(max_words[0])

if __name__ == '__main__':
    main()