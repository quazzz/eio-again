n,x = map(int,input().split())
a = sorted(list(map(int,input().split())))
ans  = 0
for i in range(n):
    x-= a[i]
    if x >= 0:
        ans += 1 
    else:
        break
print(ans)
