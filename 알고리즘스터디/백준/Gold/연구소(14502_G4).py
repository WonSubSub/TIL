from collections import deque
N, M = map(int, input().split())
lab = []
for i in range(N):
    lab.append(list(map(int, input().split())))

#예외처리 1.빈 q에서 pop, 2. matrix index 벗어나는 move
default = 0
for x in range(N):
    for y in range(M):
        if lab[x][y] == 1:
            default += 1

def bfs(visit, lab, q):
    current = q.popleft()
    x, y = current[0], current[1]
    moves = [[1,0],[0,1],[-1,0],[0,-1]]
    for a, b in moves:
        if 0 <= x+a <= N-1 and 0 <= y+b <= M-1:
            if lab[x+a][y+b] == 0 and visit[x+a][y+b] == 0:
                q.append([x+a, y+b])
                visit[x+a][y+b] = 1
    if len(q) == 0:
        return visit
    else:
        return bfs(visit, lab, q)

zero_list = []
for x in range(N):
    for y in range(M):
        if lab[x][y] == 0:
            zero_list.append([x,y])

ans_list = []
for a in range(len(zero_list)):
    for b in range(a+1, len(zero_list)):
        for c in range(b+1, len(zero_list)):
            lab[zero_list[a][0]][zero_list[a][1]] = 1
            lab[zero_list[b][0]][zero_list[b][1]] = 1
            lab[zero_list[c][0]][zero_list[c][1]] = 1

            visit = [[0] * M for _ in range(N)]
            for x in range(N):
                for y in range(M):
                    if lab[x][y] == 2:
                        visit[x][y] = 2
                        q = deque()
                        q.append([x,y])
                        bfs(visit, lab, q)

            zeros = 0
            for x in range(N):
                for y in range(M):
                    if visit[x][y] == 0:
                        zeros += 1
            ans_list.append(zeros - default - 3)

            lab[zero_list[a][0]][zero_list[a][1]] = 0
            lab[zero_list[b][0]][zero_list[b][1]] = 0
            lab[zero_list[c][0]][zero_list[c][1]] = 0

answer = max(ans_list)
print(answer)