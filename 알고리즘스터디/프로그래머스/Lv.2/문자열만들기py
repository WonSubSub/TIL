def solution(s):
    answer = []
    
    s = s.lower()
    
    blank = []
    for i in range(len(s)):
        if s[i] == ' ':
            blank.append(i)
            
    words = list(map(str, s.split()))
    for word in words:
        for i in range(len(word)):
            if i == 0:
                answer.append(word[i].upper())
            else:
                answer.append(word[i])
    
    for i in blank:
        answer.insert(i, ' ')
    
    answer = ''.join(answer)
    
    return answer