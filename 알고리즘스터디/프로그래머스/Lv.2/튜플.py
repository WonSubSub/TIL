def solution(s):
    answer = []
    s = s[2:-2]
    s = s.replace('},{', '.')
    s = s.split('.')
    for i in range(len(s)):
        s[i] = list(map(int, s[i].split(',')))
    
    for i in range(len(s)):
        for a in range(len(s)):
            if len(s[a]) == i+1:
                for num in s[a]:
                    if num not in answer:
                        answer.append(num)
                break
                
    return answer