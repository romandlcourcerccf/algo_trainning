import os
from collections import defaultdict, Counter
def main():

    dir_name = os.path.dirname(__file__)
    # filename = os.path.join(dir_name, "1.txt")
    filename = os.path.join(dir_name, "input.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

   
    # print(rows[1])
    # print(rows[2])

    pattern = Counter(rows[1])
    pattern = list(rows[1])
    phrase = list(rows[2])
    pattern_dict =  Counter(pattern)
    window = defaultdict(int)
  
    hit_count = 0
    for r  in range(0, len(phrase)-len(pattern)+1):

        s_string = phrase[r: r+len(pattern)]
        # print(s_string)
        s_string_dict = Counter(s_string)
        if len(s_string_dict) == len(pattern_dict):
            is_same = True
            for c in s_string_dict:
                if c not in pattern_dict:
                    is_same = False
                    break
                elif s_string_dict[c] < pattern_dict[c] or s_string_dict[c] > pattern_dict[c]:
                    is_same = False
                    break

            if is_same:
                hit_count +=1

    print(hit_count)



if __name__ == '__main__':
    main()
