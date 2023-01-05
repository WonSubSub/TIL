def solution(num):
    answer = 0
    
    def make_one(num, answer):
        if num % 2 == 0:
            answer += 1
            if int(num/2) == 1:
                return answer
            answer = make_one(int(num/2), answer)
            return answer
        if num % 2 == 1:
            answer += 1
            if num == 1:
                return answer
            answer = make_one(num*3 + 1, answer)
            return answer
    answer = make_one(num, answer)
    
    if answer > 500:
        answer = -1
    
    if num == 1:
        answer = 0
        
    return answer