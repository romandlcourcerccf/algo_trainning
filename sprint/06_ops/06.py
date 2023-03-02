def ops():
    lines = open('input.txt', 'r').readlines()

    mem_size, sectors_nums, sectors = int(lines[0]), int(lines[1]), lines[2:]
    
    sectors = [s.replace('\n', '').split(' ') for s in sectors]
    
    sectors = [[int(s[0]), int(s[1])] for s in sectors]

    # print('mem_size :', mem_size)
    # print('sectors_nums :', sectors_nums)
    print('sectors :', sectors)

    memory = [-1] * mem_size

    alive_sectors = len(sectors)  
    use set !!!!!
    
    for i, s in enumerate(sectors):
        erise = False
        print('i: ', i+1,'s: ', s)
        print('b :', memory)
        for r in range(s[0]-1, s[1]):
            if memory[r] > -1: erise = True
            memory[r] = i + 1
        print('a :', memory)
        if erise:
            alive_sectors -=1

    print(memory)

    print('alive_sectors :', alive_sectors)

    # open('output.txt', 'w') 

ops()



