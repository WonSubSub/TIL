def solution(n, left, right):
    answer = []
    
    a = left//n + 1
    b = right//n + 1
    for i in range(a,b+1):
        for _ in range(i):
            answer.append(i)
        for m in range(i+1, n+1):
            answer.append(m)
            
    answer = answer[left%n : left%n + right - left+1]
    return answer