def solution(x):
    answer = True
    
    x = str(x)
    x_list = list(map(int, x))
    
    if int(x) % sum(x_list) != 0:
        answer = False
    return answer