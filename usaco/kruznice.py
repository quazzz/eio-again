n = int(input())
a = []
for _ in range(n):
    x,r = map(int,input().split())
    a.append((x - r, x+ r))
a.sort(key =lambda t: -t[1])
ans = 0
last = -float('inf')
for l,r in a:
    if l>=last:
        ans+=1
        last = r
print(n - ans)