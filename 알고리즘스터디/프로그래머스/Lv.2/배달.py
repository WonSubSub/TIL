from collections import deque
def solution(N, road, K):           # bfs풀이 마을별 걸리는 최소 시간 리스트 추가
    q = deque([[1,K]])
    ans_set = set([1])
    cost = [0] * (N+1)

    while q:
        current, K = q.popleft()
        temp = len(q)
        for i in range(len(road)):
            if road[i][0] == current:
                if road[i][2] <= K:
                    if K-road[i][2] >= cost[road[i][1]]:
                        cost[road[i][1]] = K-road[i][2]
                        ans_set.add(road[i][1])
                        q.append([road[i][1], K-road[i][2]])
            if road[i][1] == current:
                if road[i][2] <= K:
                    if K-road[i][2] >= cost[road[i][0]]:
                        cost[road[i][0]] = K-road[i][2]
                        ans_set.add(road[i][0])
                        q.append([road[i][0], K-road[i][2]])
    answer = len(ans_set)
    
    return answer

def solution(N, road, K):           # dfs풀이 --> 32번테케 시간초과
    ans_set = set([1])
    current = 1
    visit = [0] * (N+1)
    visit[1] = 1
    def dfs(visit, K, road, ans_set, current):
        for i in range(len(road)):
            if road[i][0] == current:
                if road[i][2] <= K and visit[road[i][1]] == 0:
                    ans_set.add(road[i][1])
                    visit[road[i][1]] = 1
                    dfs(visit, K-road[i][2],road,ans_set,road[i][1])
                    visit[road[i][1]] = 0                   
            elif road[i][1] == current:
                if road[i][2] <= K and visit[road[i][0]] == 0:
                    ans_set.add(road[i][0])
                    visit[road[i][0]] = 1
                    dfs(visit, K-road[i][2],road,ans_set,road[i][0])
                    visit[road[i][0]] = 0
        return ans_set
    
    answer = len(dfs(visit, K, road, ans_set, current))

    return answer