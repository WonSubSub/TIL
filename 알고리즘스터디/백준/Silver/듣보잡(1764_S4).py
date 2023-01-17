import sys
input = sys.stdin.readline

n, m = map(int, input().split())

n_dict = {}
ans = []
for i in range(n):
    n_dict[input().strip()] = 0

cnt = 0
for i in range(m):
    name = input().strip()
    if name in n_dict.keys():
        cnt += 1
        ans.append(name)

ans.sort()
print(cnt)
for i in range(len(ans)):
    print(ans[i])