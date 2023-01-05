def solution(s):
    answer = True
    
    word = list(map(str, s.lower()))
    if word.count('p') == word.count('y'):
        answer = True
    elif word.count('p') != word.count('y'):
        answer = False

    return answer