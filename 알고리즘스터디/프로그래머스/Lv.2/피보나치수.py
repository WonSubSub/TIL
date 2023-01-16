import sys
sys.setrecursionlimit(10**6)

def solution(n):
    answer = 0
    
    first = 0
    second = 1
    pibo_i = 1
    
    def pibo(first, second, pibo_i):
        pibo_i += 1
        if pibo_i == n:
            return first + second
        else:
            return pibo(second, first + second, pibo_i)
    
    pibo_num = pibo(first, second, pibo_i)
    answer = pibo_num % 1234567
    
    return answer