def solution(n):
    answer = 0
    
    def pac(num):
        ans = 1
        for i in range(1, num+1):
            ans = ans * i
        return ans
    
    def res(a, b):
        ans = int(pac(a+b) // (pac(a) * pac(b)))
        return ans
    
    for i in range(int(n/2)+1):
        one_num = n - i*2
        two_num = i
        answer += res(one_num, two_num)
        # print(res(one_num,two_num) , one_num, two_num)
    
    answer = answer % 1234567
    return answer