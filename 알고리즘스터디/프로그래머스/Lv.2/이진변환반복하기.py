def solution(s):
    zero_cnt = 0
    cnt = 0
    
    def get_ans(s, cnt, zero_cnt):
        cnt += 1
        zero_cnt += s.count('0')
        s = s.replace('0', '')
        if s == '1':
            return cnt, zero_cnt
        else:
            c = len(s)
            max_i = get_max(c)
            s = make_two(c, max_i)
            return get_ans(s, cnt, zero_cnt)

    def get_max(c):
        temp = 1
        temp_cnt = 0
        while temp <= c:
            temp = temp*2
            temp_cnt += 1
        return temp_cnt - 1
    
    def make_two(c, max_i):
        new_s = ''
        for i in range(max_i, -1, -1):
            new_s += str(c // (2**i))
            c = c % (2**i)
        return new_s
    
    cnt, zero_cnt = get_ans(s, cnt, zero_cnt)
    answer = [cnt, zero_cnt]
    
    return answer