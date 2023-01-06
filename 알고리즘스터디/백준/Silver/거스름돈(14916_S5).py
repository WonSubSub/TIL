n = int(input())

ans = 0
for i in range(1, 1000000):
    temp_n = n - i * 2
    if temp_n < 0:
        ans = -1
        break
    if temp_n % 5 == 0:
        ans += i
        ans += temp_n//5
        break

if n % 5 == 0:
    ans = n//5

print(ans)