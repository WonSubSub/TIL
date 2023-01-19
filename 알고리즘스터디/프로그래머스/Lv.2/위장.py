def solution(clothes):
    answer = 1
    
    clothes_dict = {}
    for clothe in clothes:
        if clothe[-1] not in clothes_dict.keys():
            clothes_dict[clothe[-1]] = 2
        else:
            clothes_dict[clothe[-1]] += 1
    
    if len(clothes_dict.values()) == 1:
        answer = list(clothes_dict.values())[0] - 1
    else:
        for i in list(clothes_dict.values()):
            answer = answer * i
        answer -= 1
    
    return answer