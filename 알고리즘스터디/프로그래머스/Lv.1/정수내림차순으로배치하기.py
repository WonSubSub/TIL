def solution(n):
    answer = 0
    n = str(n)
    n_list = list(map(int, n))
    n_list.sort(reverse = True)
    n_list = list(map(str, n_list))
    answer = int("".join(n_list))
    
    return answer