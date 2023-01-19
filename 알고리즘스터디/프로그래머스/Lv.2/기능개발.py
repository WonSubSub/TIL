from collections import deque

def solution(progresses, speeds):
    answer = []
    
    days = deque()
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            days.append((100 - progresses[i]) // speeds[i])
        else:
            days.append((100 - progresses[i]) // speeds[i]+1)
    
    while len(days) != 0:
        cnt = 1
        day = days.popleft()
        while len(days) != 0 and days[0] <= day:
            cnt += 1
            days.popleft()
        answer.append(cnt)  
    
    return answer