def ops():
    lines = open('input.txt', 'r').readlines()

    mem_size, sectors_nums, sectors = int(lines[0]), int(lines[1]), lines[2:]
    
    sectors = [s.replace('\n', '').split(' ') for s in sectors]
    
    sectors = [[int(s[0]), int(s[1])] for s in sectors]


    memory = [-1] * mem_size

    alive_sectors = set(range(1,len(sectors)+1))
    
    for i, s in enumerate(sectors):
        to_arise = set()

        for r in range(s[0]-1, s[1]):
            if memory[r] > -1:
                to_arise.add(memory[r])
            memory[r] = i + 1
       
        if len(to_arise) > 0:
            alive_sectors = alive_sectors - to_arise

   
    open('output.txt', 'w').write(str(len(alive_sectors))) 

ops()



