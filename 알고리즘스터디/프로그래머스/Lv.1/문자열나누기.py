import sys
sys.setrecursionlimit(10**6)

def solution(s):
    answer = 0
    
    def split_str(s,answer):
        answer += 1
        x = s[0]
        x_cnt = 1
        other_cnt = 0
        for i in range(1, len(s)):
            if s[i] == x:
                x_cnt += 1
            else:
                other_cnt += 1
                if x_cnt == other_cnt:
                    index = i
                    if index+1 == len(s):
                        break
                    else:
                        s = s[index+1:]
                        return split_str(s, answer)
        return answer
                        
    answer = split_str(s, answer)
        
    return answer