lipud = list(map(int,input().split()))
n = 8
sols = []
def backtrack(row, cols, diag1, diag2, cur):
    if row == n:
        sols.append(cur[:])
        return
    for col in range(1, n+ 1):
        if col not in cols and (row - col) not in diag1 and (row + col) not in diag2:
            cur.append(col)
            backtrack(row+1, cols|{col}, diag1|{row-col}, diag2|{row+col}, cur)
            cur.pop()
backtrack(0, set(), set(), set(), [])
best=  8
for sol in sols:
    diff = sum(1 for i in range(8) if sol[i] != lipud[i])
    best = min(diff,best)
print(best)