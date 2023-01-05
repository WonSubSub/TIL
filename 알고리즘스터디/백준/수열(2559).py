n, k = map(int, input().split())
temperatures = list(map(int, input().split()))

sum_list = [-100000] * k
sum_list.append(sum(temperatures[:k+1]))

for i in range(k, n):
        sum_list.append(sum_list[i] + temperatures[i] - temperatures[i-k])

print(max(sum_list))

# ans_index = k-1
# for i in range(k, n):
#     if temperatures[i] > temperatures[i-k]:
#         ans_index = i
#         temp_ans = sum(temperatures[ans_index-k+1:ans_index+1])
#         if temp_ans > ans:
#             ans = temp_ans

# ans_list = []
# for i in range(k-1, n):
#     ans_list.append(sum(temperatures[i-k+1:i]))
# ans = max(ans_list)