def solution(X, Y):
    answer = ''
    
    numbers = [0,1,2,3,4,5,6,7,8,9]
    final = [0,0,0,0,0,0,0,0,0,0]
    
    for i in numbers:
        num = str(i)
        if num in Y:
            final[i] = min(X.count(str(i)), Y.count(str(i)))
    
    if final[1:] == [0,0,0,0,0,0,0,0,0]:
        if final[0] > 0:
            answer = '0'
        else:
            answer = '-1'
    else: 
        for i in range(len(final)-1,-1,-1):
            answer += str(i) * final[i]
        
    return answer