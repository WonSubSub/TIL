def solution(topping):
    answer = 0
    
    left_set = set()
    right_set = set()
    left_cnt = [0]
    right_cnt = [0]
    for i in range(len(topping)):
        left_set.add(topping[i])
        right_set.add(topping[-(i+1)])
        left_cnt.append(len(left_set))
        right_cnt.append(len(right_set))
    for i in range(len(topping)):
        if left_cnt[i] == right_cnt[-(i+1)]:
            answer += 1
    return answer