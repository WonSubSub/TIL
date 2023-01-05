n = int(input())

def get_sum(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

def get_value(numbers, sum):
    value = 0
    for i in range(len(numbers)):
        for a in range(i+1, len(numbers)):
            temp_value = (sum - numbers[a] - numbers[i]) % 10
            if temp_value > value:
                value = temp_value
    return value

ans = 0
ans_value = 0

for i in range(n):
    numbers = list(map(int, input().split(' ')))

    sum = get_sum(numbers)
    value = get_value(numbers, sum)

    if value >= ans_value:
        ans_value = value
        ans = i + 1
    # print(value, ans)

print(ans)