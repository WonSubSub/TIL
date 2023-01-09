def solution(answers):
    answer = []
    
    one = [1, 2, 3, 4, 5] * 2000
    two = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    
    cnt = [[1,0], [2,0], [3,0]]
    cnt_list = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == one[i]:
            cnt[0][1] += 1
            cnt_list[0] += 1
        if answers[i] == two[i]:
            cnt[1][1] += 1
            cnt_list[1] += 1
        if answers[i] == three[i]:
            cnt[2][1] += 1
            cnt_list[2] += 1
    
    for i in range(3):
        if cnt[i][1] == max(cnt_list):
            answer.append(cnt[i][0])
            
    return answer