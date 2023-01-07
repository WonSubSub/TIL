def solution(d, budget):
    answer = 0
    d.sort()
    
    for money in d:
        budget -= money
        answer += 1
        if budget <= 0:
            break
    
    if budget < 0:
        answer -= 1
    return answer