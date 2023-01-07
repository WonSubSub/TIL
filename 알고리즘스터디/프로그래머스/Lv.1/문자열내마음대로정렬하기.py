def solution(strings, n):
    answer = []
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    
    second = []
    for i in range(len(strings)):
        second.append(strings[i][n])
    print(second)
    
    for alphabet in alphabets:
        temp_answer = []
        while alphabet in second:
            temp_answer.append(strings[second.index(alphabet)])
            strings.pop(second.index(alphabet))
            second.pop(second.index(alphabet))
        temp_answer.sort()
        answer.extend(temp_answer)
    return answer