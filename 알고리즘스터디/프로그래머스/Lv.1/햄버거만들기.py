def solution(ingredient):
    answer = 0
    
    new_in = ''
    for i in ingredient:
        new_in += str(i)
        if new_in[-4:] == '1231':
            new_in = new_in[:-4]
            answer += 1
    
    return answer