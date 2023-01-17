from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    q = deque()
    if cacheSize == 0:
        answer = len(cities) * 5
    else:
        for city in cities:
            if city.lower() not in q:
                if len(q) == cacheSize:
                    q.popleft()
                    q.append(city.lower())
                    answer += 5
                else:
                    q.append(city.lower())
                    answer += 5
            else:
                q.remove(city.lower())
                q.append(city.lower())
                answer += 1
    
    return answer