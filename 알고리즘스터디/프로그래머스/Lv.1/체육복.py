def solution(n, lost, reserve):
    answer = n
    
    lost, reserve = sorted(list(set(lost) - set(reserve))), sorted(list(set(reserve) - set(lost)))
    
    for i in lost:
        if i - 1 in reserve:
            reserve.remove(i-1)
        elif i + 1 in reserve:
            reserve.remove(i+1)
        else:
            answer -= 1
    return answer