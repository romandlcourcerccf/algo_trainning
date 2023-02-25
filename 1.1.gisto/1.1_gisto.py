from collections import defaultdict

def run():

    with open('input.txt', 'r') as f:
        t = f.readlines()
        d = defaultdict(int)
        for l in t:
            for c in l:
                d[c] +=1
        
        if '\n' in d:
            del d['\n']
        
        if ' ' in d:
            del d[' ']

        height = max(d.values())
        thresh = min(d.values())

        res = []
        last = []
        for _,k in enumerate(d.keys()):
            res.append([k, d[k]])
            last.append(d[k])

        res.sort(key= lambda x: x[0])
        last = [c[0] for c in res]
        last = ''.join(last)

        res_ = ''
        for h in reversed(range(height)):
           
            row = ''
            for cnt in res:
                p = ' ' if cnt[1] - thresh < h else '#'
                row = row + p
            print(row)
            res_ = res_ + row + '\n'
            
        res_ = res_ + last + '\n'

        with open('output.txt', 'w') as writer:
            writer.write(res_)

if __name__ == '__main__':
    run()