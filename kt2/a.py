from bisect import bisect_left
n,m = map(int,input().split())
hinnad = [int(input()) for _ in range(n)]
soovitud = [int(input()) for _ in range(m)]

ans = []

for soov in soovitud:
    i = bisect_left(hinnad, soov)
    if i == 0:
        ans.append(hinnad[0])
    elif i == n:
        ans.append(hinnad[-1])
    else:
        vasak = hinnad[i - 1]
        parem = hinnad[i]
        if soov - vasak <= parem - soov:
            ans.append(vasak)
        else:
            ans.append(parem)
print(*ans)