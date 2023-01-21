from collections import deque           # bfs풀이
import sys
sys.setrecursionlimit(10**6)
moves = [[1,0], [0,1], [-1,0], [0,-1]]
answer = 0

def solution(maps):
    
    q = deque([[0,0,1]])
    def bfs(maps, q):
        global moves, answer
        n = len(maps)
        m = len(maps[0])
        current = q.popleft()
        x, y, answer = current[0], current[1], current[2]
        for a,b in moves:
            if [x+a,y+b] == [n-1,m-1]:
                return answer+1
            if 0<=x+a<=n-1 and 0<=y+b<=m-1 and maps[x+a][y+b] == 1:
                maps[x+a][y+b] = 0
                q.append([x+a,y+b,answer+1])
        if len(q) == 0:
            return -1
        return bfs(maps, q)

    return bfs(maps, q)



ans_list = []               # dfs풀이 --> 효율성 X
move_list = [[1,0], [0,1], [-1,0], [0,-1]]

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    start = [0,0]
    cnt = 1
    def dfs(maps,start,cnt):
        global ans_list, move_list
        x = start[0]
        y = start[1]
        for a,b in move_list:
            if 0<=x+a<=n-1 and 0<=y+b<=m-1 and maps[x+a][y+b] == 1 and maps[x+a][y+b] == 1:
                if [x+a,y+b] == [n-1,m-1]:
                    maps[x+a][y+b] = 0
                    ans_list.append(cnt+1)
                    maps[x+a][y+b] = 1
                    break
                else:
                    if len(ans_list) > 0 and cnt > max(ans_list):
                        break
                    maps[x+a][y+b] = 0
                    dfs(maps, [x+a,y+b], cnt+1)
                    maps[x+a][y+b] = 1
                    
        return ans_list
    
    ans_list = dfs(maps,start,cnt)   
    if ans_list == []:
        answer = -1
    else:
        answer = min(ans_list)
    
    return answer
