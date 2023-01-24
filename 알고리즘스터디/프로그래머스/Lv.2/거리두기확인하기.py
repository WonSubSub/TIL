from collections import deque
def solution(places):
    answer = []
    
    def bfs(visit, place, q):
        x, y , length = q.popleft()
        visit[x][y] = 1
        moves = [[1,0], [0,1], [-1,0], [0,-1]]
        for a, b in moves:
            if 0<=x+a<=4 and 0<=y+b<=4:
                if place[x+a][y+b] == 'O' and visit[x+a][y+b] == 0:
                    visit[x+a][y+b] = 1
                    q.append([x+a,y+b,length+1])
                if place[x+a][y+b] == 'P' and visit[x+a][y+b] == 0:
                    return length + 1
        if len(q) == 0:
            return 10
        return bfs(visit, place, q)
                            
    for place in places:
        moves = [[1,0], [0,1], [-1,0], [0,-1]]
        ans_list = []
        for x in range(5):
            for y in range(5):
                if place[x][y] == 'P':
                    q = deque([[x,y,0]])
                    start = [x,y,0]
                    visit = [[0] * len(place) for x in range(len(place[0]))]
                    ans_list.append(bfs(visit, place, q))
        print(ans_list)
        if ans_list == []:
            answer.append(1)
        else:
            if min(ans_list) < 3:
                answer.append(0)
            else:
                answer.append(1)
                            
    return answer
