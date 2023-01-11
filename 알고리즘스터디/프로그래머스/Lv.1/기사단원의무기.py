def solution(number, limit, power):
    answer = 0
    
    def get_yak(num):
        cnt = 0
        for i in range(1,int(num**0.5)+1):
            if num % i == 0:
                cnt += 2
                
        if int(num**0.5) - num**0.5 == 0:
            cnt -= 1
        if num == 2 or num == 3:
            cnt = 2
        if cnt > limit:
            return power
        return cnt
    
    for num in range(1,number+1):
        answer += get_yak(num)
    return answer