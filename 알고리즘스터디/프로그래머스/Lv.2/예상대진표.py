def solution(n,a,b):
    answer = 1
    a, b = min(a,b), max(a,b)
    
    if b - a == 1 and int(a/2) + 1 == int(b/2):
        answer = 1
    else: 
        while True:
            if a%2 == 0:
                a = int(a/2)
            else:
                a = int(a/2) + 1

            if b%2 == 0:
                b = int(b/2)
            else:
                b = int(b/2) + 1
                
            if b - a == 1 and int(a/2) + 1 == int(b/2):
                answer += 1
                break
            else:
                answer += 1
        
    return answer