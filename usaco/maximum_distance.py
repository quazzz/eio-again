import math
n=  int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
maks = float('-inf')
distances = []
for i in range(n):
    distances.append([x[i], y[i]])

for i in range(n):
    for j in range(i+1, n):
        maks = max((distances[j][0] - distances[i][0] ) ** 2 + (distances[j][1] - distances[i][1]) ** 2, maks)
print(maks)