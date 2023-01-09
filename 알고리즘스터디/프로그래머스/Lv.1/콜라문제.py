import sys
sys.setrecursionlimit(10000)

def solution(a, b, n):
    answer = 0
    
    def make_leftover(a, b, n, answer):
        if n < a:
            return answer
        else:
            answer += (n//a) * b
            n = n - (n//a) * a + (n//a) * b
            return make_leftover(a, b, n, answer)
        
    answer = make_leftover(a, b, n ,answer)
    return answer