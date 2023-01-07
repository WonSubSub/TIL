def solution(s):
    answer = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    blank = []
    for i in s:
        if i.lower() in alphabet:
            if count % 2:
                answer += i.lower()
            else:
                answer += i.upper()
            count += 1
        else:
            answer += i
            count = 0
    
    return answer