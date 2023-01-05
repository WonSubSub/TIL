n = int(input())

ans = 0

# for a in range(1, int(n/3) + 1):
#     for b in range(a, int((n - a)/2)+1):
#         c = n - a - b
#         if a + b > c:
#             ans += 1

if n/2 == int(n/2):
    long = int(n/2 - 1)
else:
    long = int(n/2)

for i in range(int(n/3), long+1):
    
    if (n-i)/2 == int((n-i)/2):
        second = int((n-i)/2)
    else:
        second = int((n-i)/2 + 1)

    ans += (i+1 - second)

print(ans)