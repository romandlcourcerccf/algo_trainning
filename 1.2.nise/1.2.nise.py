def nice():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        spt = int(lines[0])
        _str = lines[1]

        # print('spt :', spt)
        # print('str :', str)

    max_beauty = -1
    for i in range(len(_str)-1):
        # print(str[i])
        if i+1 + spt >= len(_str)-1:
            max_beauty = max(max_beauty, len(_str)-1 - i)
        elif _str[i+1 + spt] != _str[i]:
            max_beauty = max(max_beauty, spt)
        else:
            _i =  i+1 + spt
            while _str[_i] == _str[i] and _i < len(_str)-1:
                _i  +=1
            max_beauty = max(max_beauty, _i - i)
       

    with open('output.txt', 'w') as w:
        # print(str(max_beauty))
        w.write(str(max_beauty))

if __name__ == '__main__':
    nice()