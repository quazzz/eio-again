n,q  = map(int,input().split())
updates = {}
queries = {}
coords=  set()

for _ in range(n):
    l,r,v = map(int,input().split())
    updates.append((l,r, v))
    coords.add(l)
    coords.add(r)
for _ in range(q):
    l,r = map(int,input().split())
    queries.append((l,r))
    coords.add(l)
    coords.add(r)
coords = sorted(coords)
idx = {x: i for i, x in enumerate(coords)}
diff = [0] * (len(coords) + 1)
for l,r,v in updates:
    diff[idx[l]] += v
    diff[idx[r]] -= v
pref = [0] * len(coords)
cur = 0
for i in range(len(coords) - 1):
    cur += diff[idx[i]]
    pref[i+1] = pref[i] + cur * (coords[i+1] - coords[i])
for l,r in queries:
    print(pref[idx[r]] - pref[idx[l]])