def solution(numbers):
    answer = []
    
    for num in numbers:
        jinsoo = bin(num)[2:].split('0')[-1]
        if jinsoo == '':
            answer.append(num+1)
        else:
            answer.append(num + 2**(len(jinsoo)-1))
    return answer