visit = [[0,0]]             # dfs --> 효율성 X
ans_list = []
cnt = 1
move_list = [[1,0], [0,1], [-1,0], [0,-1]]

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    start = [0,0]
    def dfs(maps,start):
        global visit, ans_list, cnt, move_list
        x = start[0]
        y = start[1]
        for a,b in move_list:
            if 0<=x+a<=n-1 and 0<=y+b<=m-1 and maps[x+a][y+b] == 1 and [x+a,y+b] not in visit:
                if [x+a,y+b] == [n-1,m-1]:
                    cnt += 1
                    visit.append([x+a,y+b])
                    ans_list.append(cnt)
                    cnt -= 1
                    break
                else:
                    cnt += 1
                    visit.append([x+a,y+b])
                    dfs(maps, [x+a,y+b])
                    visit.pop()
                    cnt -= 1
                    
        return ans_list
    
    ans_list = dfs(maps,start)   
    if ans_list == []:
        answer = -1
    else:
        answer = min(ans_list)
    
    return answer
