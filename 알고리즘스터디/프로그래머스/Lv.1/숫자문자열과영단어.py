def solution(s):
    answer = ''
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    alphabets = list(map(str, alphabets))
    strings = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer_list = []
    
    for i in range(len(s)-1, -1, -1):
        if s[i] in alphabets:
            for a in range(i-4, i):
                word = s[a:i+1]
                if word in strings:
                    answer_list.append(strings.index(word))
                    break
                    s = s[:a]
        else:
            answer_list.append(int(s[i]))
            s = s[:i]
    for i in answer_list[::-1]:
        answer += str(i)
    answer = int(answer)    
    
    return answer