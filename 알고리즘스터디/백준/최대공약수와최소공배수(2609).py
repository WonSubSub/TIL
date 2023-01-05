n, v = map(int, input().split(' '))

big = max(n,v)
small = min(n,v)
if big % small == 0:
    print(small)
    print(big)
else:
    for i in range(int(small/2), 0, -1):
        if big % i == 0 and small % i == 0:
            print(i)
            print(int(big * small / i))
            break