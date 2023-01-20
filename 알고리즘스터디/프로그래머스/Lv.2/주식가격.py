from collections import deque

def solution(prices):
    answer = deque()
    q = deque()
    
    for i in range(len(prices)-1, -1, -1):
        cnt = 0
        for a in range(len(q)):
            if q[a] > prices[i]:
                cnt += 1
            elif q[a] == prices[i]:
                cnt += answer[a] + 1
                break
            else:
                cnt += 1
                break
        answer.appendleft(cnt)
        q.appendleft(prices[i])
    answer = list(answer)

    return answer