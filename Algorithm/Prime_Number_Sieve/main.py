number= 100000
a = [0] * (number + 1)

def prime_number_sieve():
    # 초기화: a[i] = i
    for i in range(2,number+1):
        a[i] = i

    # 소수 아닌 수 지우기
    for i in range(2,number+1):
        if a[i] == 0:
            continue
        for j in range(i*2, number+1, i):
            a[j] = 0

    # 결과 출력
    for i in range(2, number+1):
        if a[i] != 0:
            print(a[i], end=' ')

prime_number_sieve()
