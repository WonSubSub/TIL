def solution(N, road, K):
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