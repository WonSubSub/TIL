from collections import deque

def solution(priorities, location):
    answer = 0
    
    sorted_pri = deque(sorted(priorities)[::-1])
    priorities = deque(priorities)
    priorities[location] = priorities[location] + 10
    my_num = priorities[location]
    
    while my_num in priorities:
        if priorities[0] % 10 < sorted_pri[0]:
            priorities.append(priorities.popleft())
        else:
            priorities.popleft()
            sorted_pri.popleft()
            answer += 1
    
    return answer