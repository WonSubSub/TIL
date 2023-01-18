import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, v = map(int, input().split())

fs = []
for i in range(m):
    nums = list(map(int, input().split()))
    fs.append(nums)
    fs.append(nums[::-1])
fs.sort()

dfs_list = [v]
def dfs(start_n, dfs_list):
    for i in range(len(fs)):
        if fs[i][0] == start_n:
            if fs[i][1] not in dfs_list:
                dfs_list.append(fs[i][1])
                dfs(fs[i][1], dfs_list)
    return dfs_list

bfs_list = [v]
bfs_q = deque([v])
def bfs(bfs_list, bfs_q):
    for i in range(len(fs)):
        if fs[i][0] == bfs_q[0]:
            if fs[i][1] not in bfs_list:
                bfs_list.append(fs[i][1])
                bfs_q.append(fs[i][1])
    bfs_q.popleft()
    if len(bfs_q) > 0:
        return bfs(bfs_list, bfs_q)
    else:
        return bfs_list

d = dfs(v, dfs_list)
b = bfs(bfs_list, bfs_q)
for i in d:
    if i == d[-1]:
        print(i)
    else:
        print(i, end=' ')
for i in b:
    if i == b[-1]:
        print(i)
    else:
        print(i, end=' ')