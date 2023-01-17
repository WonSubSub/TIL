from collections import deque

def solution(s):
    answer = 0
    
    left = ['{', '[', '(']
    right = ['}', ']', ')']
    s_q = deque(list(map(str, s)))

    for a in range(len(s_q)):
        q = deque()
        left_cnt = 0
        right_cnt = 0
        t = 0
        for i in range(len(s_q)):
            if s_q[i] in left:
                left_cnt += 1
                q.append(s_q[i])
            else:
                right_cnt += 1
                if right_cnt > left_cnt:
                    t += 1
                    break
                elif right.index(s_q[i]) != left.index(q[-1]):
                    t += 1
                    break
                else:
                    q.pop()
        if len(q) == 0 and t == 0:
            answer += 1
        s_q.append(s_q.popleft())
                
    return answer