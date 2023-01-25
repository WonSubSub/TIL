from collections import deque

def solution(jobs):
    answer = 0
    l = len(jobs)
    jobs = deque(sorted(jobs))
    time = jobs[0][0]
    while jobs:
        waiting = []
        current = jobs.popleft()
        answer += current[1]
        time += current[1]
        while jobs and jobs[0][0] <= current[1] + current[0]:
            waiting.append(jobs.popleft())
        if waiting:
            while waiting:
                waiting = list(waiting)
                waiting.sort(key= lambda x: x[1])
                waiting = deque(waiting)
                waiting[0][1] += time
                current = waiting.popleft()
                answer += current[1] - current[0]
                time = current[1]
                while jobs and jobs[0][0] <= current[1]:
                    waiting.append(jobs.popleft())
    answer = answer // l
    
    return answer