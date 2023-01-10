def solution(lottos, win_nums):
    answer = []
    winning = [6,6,5,4,3,2,1]
    
    min_win = 0
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            min_win += 1
    
    if min_win == 6:
        answer = [1,1]
    else:
        answer = [winning[min_win + lottos.count(0)], winning[min_win]]
                                                                
    return answer