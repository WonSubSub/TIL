def solution(s):
    answer = True
    
    right = 0 
    left = 0
    
    if s.count('(') == s.count(')'):
        for i in s:
            if i == '(':
                right += 1
            else:
                left += 1
            if left > right:
                answer = False
                break
    else:
        answer = False

    return answer