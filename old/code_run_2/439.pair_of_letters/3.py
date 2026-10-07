def main():
    string = input()
    splited = string.split()
    pair_map = {}
    for word in splited:
        if len(word) < 2:
            continue
        for i in range(len(word) - 1):
            pair = word[i : i + 2]
            if pair in pair_map:
                pair_map[pair] += 1
            else:
                pair_map[pair] = 1

    s_pairs = dict(sorted(pair_map.items(), key=lambda x: (-x[1], -ord(x[0][0]))))
    print(next(iter(s_pairs)))
