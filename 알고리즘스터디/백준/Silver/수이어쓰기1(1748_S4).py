n = int(input())

answer = 0
length = len(str(n))
for i in range(1, length):
    answer += 10**(i-1) * 9 * i

answer += (n-10**(length-1) + 1) * length

print(answer)