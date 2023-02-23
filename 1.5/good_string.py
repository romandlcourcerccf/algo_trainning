with open('input.txt', 'r') as r:
    lines = r.readlines()
    print('lines :', lines)

print(lines) 

lines = [int(l) for l in lines]

letters = {}    
for i,l in enumerate(lines[1:]):
    letters[i] = l

print(letters)


