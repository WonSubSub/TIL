def solution(s):
    answer = -1
    
    s_list = []
    for i in range(len(s)):
        if i == 0:
            s_list.append(s[i])
        else:
            if len(s_list) > 0:
                if s[i] == s_list[-1]:
                    s_list.pop()
                else:
                    s_list.append(s[i])
            else:
                s_list.append(s[i])
    
    if len(s_list) == 0:
        answer = 1
    else:
        answer = 0
    
    return answer