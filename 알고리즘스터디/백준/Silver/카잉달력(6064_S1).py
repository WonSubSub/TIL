n = int(input())
for i in range(n):
    m, n, x, y = map(int, input().split())
    if m > n:
        m, n, x, y = n, m, y, x
    answer = x % m
    cnt = 0
    while answer % n != y % n:
        answer += m
        cnt += 1
        if cnt > n+2:
            answer = -1
            break
    if answer == 0:
        answer = n * m
        while True:
            temp = n % m
            if temp != 0:
                n = m
                m = temp
            else:
                break
        answer = int(answer / m)
    print(answer)