import sys
input = sys.stdin.readline

n = int(input())

ranks = []
answer = 0
for i in range(n):
    rank = int(input())
    ranks.append(rank)
ranks.sort()

for i in range(n):
    answer += abs(i + 1 - ranks[i])
    
print(answer)