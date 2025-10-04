from random import choice
from string import ascii_uppercase


with open('6.txt', 'w') as f:
    f.write(''.join(choice(ascii_uppercase) for i in range(int(pow(10,5)))))
