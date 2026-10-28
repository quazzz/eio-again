from bisect import bisect_left

n  = int(input())
a = list(map(int, input().split()))
b = list(map(int,input().split()))

pos = [0] * (n + 1)

for i in range(n):
    pos[b[i]] = i
lis = []
for x in a:
    p = pos[x]
    idx =bisect_left(lis, p)
    if idx == len(lis):
        lis.append(p)
    else:
        lis[idx] = p
print(len(lis))

