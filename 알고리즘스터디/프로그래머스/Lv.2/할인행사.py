from collections import deque

def solution(want, number, discount):
    answer = 0
    
    q = deque()
    l = sum(number)
    ans_list = []
    for i in range(len(discount)-l+1):
        if i == 0:
            q = deque(discount[i:i+l])
        else:
            q.popleft()
            q.append(discount[i+l-1])
        temp_answer = 0
        for i in range(len(want)):
            if q.count(want[i]) != number[i]:
                temp_answer = 0
                break
            else:
                temp_answer = 1
        ans_list.append(temp_answer)
    answer = sum(ans_list)
    return answer