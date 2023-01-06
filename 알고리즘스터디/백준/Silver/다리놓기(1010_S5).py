n = int(input())

for i in range(n):
    a, b = map(int, input().split())

    up = 1
    down = 1
    for num in range(b, b-a, -1):
        up = up * num
    for num in range(1, a+1):
        down = down * num
    print(int(up/down))