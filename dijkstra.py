import  m_readinp
m_readinp.init(__file__)


INF = 999999999

v, e, s = [int(x) for x in input().split()]
dis = [[INF] * v for _ in range(v)]
for _ in range(e):
    t1, t2, t3 = [int(x) for x in input().split()]
    dis[t1][t2] = t3

d = [INF] * v
mark = [False] * v
d[s] = 0
while True:
    cost = INF
    choose = -1
    for x in range(v):
        if not mark[x] and d[x] < cost:
            choose = x
            cost = d[x]
            break
    if cost == INF:
        break
    mark[choose] = True
    for x in range(v):
        if not mark[x]:
            d[x] = min(d[x], d[choose] + dis[choose][x])

for i in range(v):
    print(f"{i} distance {d[i]}")

