with open('input.txt', 'r') as r:
    lines = r.readlines()

lines = [int(l) for l in lines]

letters_range = int(lines[0])
letters = lines[1:]

ans = 0
for i in range(len(letters)-1):

    if letters[i] <= letters[i+1]:
        ans += letters[i]
    elif letters[i] > letters[i+1]:
         ans += letters[i+1]

with open('output.txt', 'w') as w:
    w.write(str(ans))


