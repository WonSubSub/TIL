n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
answer = 0
for i in range(len(A)):
    if A[i] != 0:
        answer += A[i] * max(B)
        B.remove(max(B))
    else:
        B.remove(max(B))

print(answer)