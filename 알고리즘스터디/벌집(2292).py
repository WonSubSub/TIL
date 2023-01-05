n = int(input())

# x(i) = i * 2 + ((i-1) * 2 - 1) * 2

max_num = [0]
for i in range(1, 50000):
    if i == 1:
        max_num.append(1)
    else:
        numbers_count = i * 2 + ((i-1) * 2 - 1) * 2
        max_num.append(max_num[i-1] + numbers_count)
        if max_num[i-1] + numbers_count >= n:
            ans = i
            break

print(ans)