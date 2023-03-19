with open('input.txt', 'r') as w:
    lines = w.readlines()
    
M, N = int(lines[0].split(' ')[0]), int(lines[0].split(' ')[1])
V = [set() for i in range(N)]
vis = [0] * N
for e in  lines[1:]:
    e, s = int(e.split(' ')[0]), int(e.split(' ')[1])
    V[e].add(s)
    V[s].add(e)

def dfs(v, comp):
    for u in V[v]:
        if vis[u-1] == 0:
            vis[u-1] = 1
            comp.append(u)
            dfs(u,comp)

res = []
for i in range(1,len(V)):
    comp = []
    if vis[i-1] == 0:
        dfs(i, comp)

    if len(comp) > len(res):
        res = comp

res = sorted(res)
res = [str(r) for r in res]
with open('output.txt', 'w') as w:
    w.write(str(len(res)))
    w.write('\n')
    w.write(' '.join(res))


