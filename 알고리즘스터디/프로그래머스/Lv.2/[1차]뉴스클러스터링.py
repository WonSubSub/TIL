def solution(str1, str2):
    answer = 0
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    str1 = str1.lower()
    str2 = str2.lower()
    str1_list = []
    str2_list = []
    
    for i in range(len(str1)-1):
        temp = ''
        if str1[i] in alphabet:
            temp += str1[i]
        if str1[i+1] in alphabet:
            temp += str1[i+1]
        if len(temp) == 2:
            str1_list.append(temp)
            
    for i in range(len(str2)-1):
        temp = ''
        if str2[i] in alphabet:
            temp += str2[i]
        if str2[i+1] in alphabet:
            temp += str2[i+1]
        if len(temp) == 2:
            str2_list.append(temp)
            
    up = 0
    down = len(str1_list) + len(str2_list)
    for s in str1_list:
        if s in str2_list:
            str2_list.remove(s)
            up += 1
    down -= up
    if down == 0:
        answer = 1
    else:
        answer = up/down
    answer = int(answer * 65536)    
    
    return answer