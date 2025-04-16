d = [0] * 100

def dp(x):
    if x == 1:
        return 1
    if x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = dp(x-1) + dp(x-2)
    return d[x]

print(dp(30))
