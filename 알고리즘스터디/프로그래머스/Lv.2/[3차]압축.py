def solution(msg):
    answer = []
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dic = {}
    for s in alphabet:
        dic[s] = len(dic) + 1
    
    i = 0
    last = ''
    while True:
        temp = msg[i]
        if i != len(msg) - 1:
            while temp in dic.keys():
                i += 1
                if (temp+msg[i]) not in dic.keys():
                    a = temp + msg[i]
                    dic[a] = len(dic) + 1
                    if i == len(msg) -1:
                        last += msg[i]
                    break
                else:
                    temp += msg[i]
                    if i == len(msg)-1:
                        break
        answer.append(dic[temp])
        if last != '':
            answer.append(dic[last])
        if i == len(msg)-1:
            break
    return answer