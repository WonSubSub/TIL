n = int(input())

numbers = list(map(int, input().split()))

length_list = [1] * n

for i in range(n):
    temp = 1
    for a in range(i):
        if numbers[a] > numbers[i]:
            if length_list[i] + length_list[a] > temp:
                temp = length_list[i] + length_list[a]
    length_list[i] = temp

print(max(length_list))                