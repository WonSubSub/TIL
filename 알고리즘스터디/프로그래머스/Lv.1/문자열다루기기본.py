def solution(s):
    answer = True
    
    alphabet = 'abcdefgihjklmnopqrstuvwxyz'
    alphabet = alphabet + alphabet.upper()
    
    for i in range(len(s)):
        if s[i] in alphabet:
            answer = False
    
    if len(s) != 4 and len(s) != 6:
        answer = False
    return answer