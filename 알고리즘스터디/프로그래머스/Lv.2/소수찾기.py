import sys
sys.setrecursionlimit(10**6)

def solution(numbers):
    answer = 0
    def check(num):
        result = True
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                result = False
                break
        return result
    
    all_num = set()
    visit = [0] * len(numbers)
    num = ''
    def dfs(visit, numbers, l, all_num, num):
        for i in range(len(numbers)):
            if visit[i] == 0:
                if len(num) == l-1:
                    all_num.add(int(num+numbers[i]))
                else:
                    visit[i] = 1
                    dfs(visit, numbers, l, all_num, num+numbers[i])
                    visit[i] = 0
        return all_num
    for i in range(1,len(numbers)+1): 
        dfs(visit, numbers, i, all_num, num)
    
    for num in list(all_num):
        if num == 1 or num == 0:
            continue
        else:
            if check(num):
                answer += 1
    return answer