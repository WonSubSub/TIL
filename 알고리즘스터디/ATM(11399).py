n = int(input())
times = sorted(list(map(int, input().split(' '))))

sum = 0

for i in range(n):
    for a in range(i+1):
        sum += times[a]

print(sum)