def solution(n):
    answer = n
    
    numbers = [1] * (n+1)
        
    for i in range(2, int(n**0.5)+1):
        for a in range(i, n+1, i):
            if a != i:
                if numbers[a]: 
                    if a % i == 0:
                        numbers[a] = 0
                        answer -= 1
                        
    answer -= 1
    
    return answer