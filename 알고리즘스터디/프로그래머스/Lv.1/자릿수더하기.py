def solution(n):
    answer = 0
    
    ans_list = []
    n = str(n)
    
    for i in range(len(n)):
        ans_list.append(int(n[i]))
    
    answer = sum(ans_list)

    return answer

# def solution(number):
#     if number < 10:
#         return number;
#     return (number % 10) + solution(number // 10) 