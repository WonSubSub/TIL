def solution(s):
    answer = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = alphabet[::-1]
    alphabet = alphabet + alphabet.upper()
    alphabet = list(map(str, alphabet))
    s = list(map(str, s))
    
    for i in alphabet:
        while i in s:
            answer += i
            s.remove(i)
    
    return answer