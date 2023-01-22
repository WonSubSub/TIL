def solution(n):
    answer = ''
    while n != 0:
        answer += str(n%3)
        if n%3 == 0:
            n = (n - 3)//3
        else:
            n = n//3
    answer = answer[::-1]
    answer = answer.replace('0','4')
    return answer
