def solution(n):
    answer = []
    
    n = str(n)
    n = n[::-1]
    
    for i in range(len(n)):
        answer.append(int(n[i]))
    
    return answer