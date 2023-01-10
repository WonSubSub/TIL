def solution(s):
    answer = []
    alphabet = [0] * len(s)
    
    for i in range(len(s)):
        if s[i] in alphabet:
            index = len(s) - 1 - alphabet[::-1].index(s[i])
            alphabet[i] = s[i]
            answer.append(i - index)
        else:
            alphabet[i] = s[i]
            answer.append(-1)
    return answer