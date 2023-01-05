def solution(n):
    answer = 0
    
    for i in range(1, int(n/2) + 1):
        if n % i == 0:
            answer += i
    answer += n

    # def get_ans(number, yaksoo):
    #     count_list = []
    #     for i in range(yaksoo + 1, int(number/2)):
    #         if number % i == 0:
    #             count_list.append(n // i)
    #             yaksoo = i
    #         break
    #     count_list = get_ans(n/yaksoo, yaksoo)
    #     return count_list
    # count_list = get_ans(n, 1)
    
    # answer = sum(count_list) + len(count_list)

    return answer