n = int(input())

ans = 0
for a in range(1, int(n/3) + 1):
    for b in range(a, int((n - a)/2)+1):
        c = n - a - b
        if a + b > c:
            ans += 1

print(ans)