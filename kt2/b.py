tulu, kulu = map(int,input().split())
best = float('-inf')

for mask in range(1 << 12):
    months = []
    for i in range(12):
        if mask & (1 << i):
            months.append(-kulu)
        else:
            months.append(tulu)
    valid=True
    for i in range(8):
        tot = 0
        for j in range(i, i + 5):
            tot += months[j]
        if tot >= 0:
            valid=False
            break
    if valid:
        result = sum(months)
        best = max(best, result)
print(best)