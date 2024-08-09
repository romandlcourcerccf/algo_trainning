import sys

    all_rows = sys.stdin.readlines() 
    exp_count = int(all_rows[0])

    exp_info = 0
    while exp_info < exp_count-1:
        exp_info +=1
        sb_count = int(all_rows[exp_info])
        exp_info +=1
        sbs = all_rows[exp_info].split()
        sbs = [int(s) for i in sbs]

        ph = []
        
        for i in range(len(sbs)):
            for j in range(len(sbs)):
            for j in range(len(sbs)):
                if i != j: