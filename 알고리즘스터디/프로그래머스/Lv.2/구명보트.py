from collections import deque

def solution(people, limit):
    answer = 0
    
    people.sort(reverse=True)
    people = deque(people)
    
    temp_limit = 0
    while len(people) != 0:
        temp_limit += people[0]
        people.popleft()
        if len(people) > 0:
            while True:
                temp_limit += people[-1]
                if temp_limit <= limit:
                    people.pop()
                    if len(people) == 0:
                        answer += 1
                        break
                else:
                    temp_limit = 0
                    answer += 1
                    break
        else:
            answer += 1
            break     
    
    return answer