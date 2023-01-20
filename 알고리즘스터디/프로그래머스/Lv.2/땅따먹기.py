def solution(land):
    for i in range(len(land)):
        if i == 0:
            a = land[i][0]
            b = land[i][1]
            c = land[i][2]
            d = land[i][3]
        else:
            a, b, c, d = land[i][0] + max(b,c,d), land[i][1] + max(a,c,d), land[i][2] + max(a,b,d), land[i][3] + max(a,b,c)    
    answer = max(a,b,c,d)

    return answer