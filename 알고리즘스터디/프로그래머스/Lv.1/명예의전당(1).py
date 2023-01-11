def solution(k, score):
    answer = []
    score_list = []
    
    for i in range(len(score)):
        if len(score_list) == k:
            if score[i] > min(score_list):
                score_list.remove(min(score_list))
                score_list.append(score[i])
                answer.append(min(score_list))
            else:
                answer.append(min(score_list))
        else:
            score_list.append(score[i])
            answer.append(min(score_list))
        
    return answer