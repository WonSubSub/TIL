number = sorted(list(map(int, input().split(' '))))

def sum_from_one(num):
    sum = 0
    for i in range(num+1):
        sum += i
    return sum

# [1,1,1,1]
# [3,4,6,8]
# 1, 9~1
# 2, 8~1
# 3, 7~1
# 4, 6~5
# 5, 5~4
# 8, 2~1
# 9, 1~1

ans = 0

first = number[0]
for i in range(1, first):
    for a in range(1, 10 - i):
        ans += sum_from_one(a)

second = number[1]
for i in range(1, second):
    ans += sum_from_one(i)

third = number[2]
for i in range(1, third):
    ans += 10 - i

fourth = number[3]
ans += fourth - 1

if (first, second, third) == (1, 1, 1):
    ans += 1

print(ans)