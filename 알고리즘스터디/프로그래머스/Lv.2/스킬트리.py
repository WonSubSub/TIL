from collections import deque

def solution(skill, skill_trees):
    answer = -1
    
    ans_list = []
    for player in skill_trees:
        new_s = ''
        temp_ans = 1
        for i in range(len(player)):
            if player[i] in skill:
                new_s += player[i]
        q = deque(map(str, skill))
        for i in range(len(new_s)):
            if new_s[i] != q[0]:
                temp_ans = 0
                break
            else:
                q.append(q.popleft())
        ans_list.append(temp_ans)
    answer = sum(ans_list)
        
    return answer