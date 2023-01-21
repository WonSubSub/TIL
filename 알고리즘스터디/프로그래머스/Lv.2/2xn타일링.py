def solution(n):
    answer = 0

    num1 = 0
    num2 = 1
    cnt = 0
    while cnt != n+1:
        cnt += 1
        num1, num2 = num2, num1+num2
    answer = num1%1000000007
    return answer