def solution(k, tangerine):
    answer = 0
    
    cnt_dict = {}
    for i in tangerine:
        if i in cnt_dict.keys():
            cnt_dict[i] += 1
        else:
            cnt_dict[i] = 1
            
    cnt_list = list(cnt_dict.values())
    cnt_list.sort(reverse=True)
    
    for cnt in cnt_list:
        k -= cnt
        answer += 1
        if k <= 0:
            break
    
    return answer