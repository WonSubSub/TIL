def solution(n, t, m, p):
    answer = ''
    num_str = '0123456789ABCDEF'
    p = p
    cnt = 0
    for i in range(1000000):
        num = ''
        while True:
            num += num_str[i%n]
            i = i//n
            if i == 0:
                break
        num = num[::-1]
        for a in range(len(num)):
            cnt += 1
            if cnt%m == p%m:
                answer += num[a]
                if len(answer) == t:
                    break
        if len(answer) == t:
            break 
    
    return answer