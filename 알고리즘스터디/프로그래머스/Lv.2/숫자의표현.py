def solution(n):
    answer = 0
    
    temp_n = n
    for i in range(2, n):
        temp_n -= i - 1
        if (temp_n // i) == 0:
            break
        else:
            if temp_n % i == 0:
                answer += 1
    answer += 1
    return answer