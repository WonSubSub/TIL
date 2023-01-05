def solution(left, right):
    answer = 0
    
    def yaksoo_count(number):
        count = 0
        for i in range(1, number+1):
            if number % i == 0:
                count += 1
        return count
    
    for number in range(left, right+1):
        if yaksoo_count(number) % 2 == 0:
            answer += number
        else:
            answer -= number
                
    return answer