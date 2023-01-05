def solution(n, m):
    answer = []
    
    n, m = min(n,m), max(n,m)
    
    for i in range(n, 0, -1):
        if m % i == 0 and n % i == 0:
            answer.append(i)
            break
    
    answer.append(max(n,m) * min(n,m) / i)
        
    return answer