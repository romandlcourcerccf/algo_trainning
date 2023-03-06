def is_intersects(sector_1, sector_2):
    a, b, c, d = sector_1[0], sector_1[1], sector_2[0], sector_2[1]
    return a <= d and c <= b

def ops():
    lines = open('input.txt', 'r').readlines()

    mem_size, sectors_nums, sectors = int(lines[0]), int(lines[1]), lines[2:]
    
    sectors = [s.replace('\n', '').split(' ') for s in sectors]
    
    sectors = [(int(s[0]), int(s[1])) for s in sectors]

    alive_sectors = set()

    for sector in sectors:
        to_del = set()
        for alive_sector in alive_sectors:
            if is_intersects(sector, alive_sector):
                to_del.add(alive_sector)
        
        alive_sectors = alive_sectors - to_del
        alive_sectors.add(sector)

    
    # print(len(alive_sectors))
    open('output.txt', 'w').write(str(len(alive_sectors))) 

ops()



