def solution(k, dungeons):          # Dfs풀이
    answer = 0
    
    visit = [0] * len(dungeons)
    cnt = 0
    ans_list = []
    def dfs(visit, cnt, dungeons, k):
        ans_list.append(cnt)
    
        for i in range(len(dungeons)):
            if visit[i] == 0:
                visit[i] = 1
                if dungeons[i][0] <= k:
                    dfs(visit, cnt+1, dungeons, k-dungeons[i][1])
                visit[i] = 0
        
    dfs(visit, cnt, dungeons, k)
    answer = max(ans_list)
    return answer