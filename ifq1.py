N = int(input())
s_list = list(map(int, input().split()))
M = int(input())
e_list = list(map(int, input().split()))
print(' '.join(str(1 if k in s_list else 0) for k in e_list))

