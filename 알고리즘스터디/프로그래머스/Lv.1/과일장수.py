def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)
    min_list = []
    for i in range((len(score)//m)*m):
        if (i+1) % m == 0:
            min_list.append(score[i])
    answer = m * sum(min_list)
    return answer