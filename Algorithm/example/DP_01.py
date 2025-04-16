d = [0] * 1001

def dp(x):
    if x == 1:
        return 1
    if x == 2:
        return 2
    if d[x] != 0:
        return d[x] # 이미 계산된 값이면 바로 반환
    d[x] = (dp(x-1) + dp(x-2)) % 10007
    return d[x] # 방금 계산한 값을 반환

x = int(input())
print(dp(x))
