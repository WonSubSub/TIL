n = int(input())
numbers = list(map(int, input().split(' ')))

count = 0

for number in numbers:
    if number == 1:
        count += 1
        continue
    else:
        for i in range(int(number/2), 1, -1):
            if number % i == 0:
                count += 1
                break

print(n - count)