def solution(n, k):
    answer = 0
    
    def ind(n, k):
        cnt = 0
        while True:
            temp = k**cnt
            if temp > n:
                break
            else:
                cnt += 1
        return cnt
    
    def jinsoo(n, k):
        max_index = ind(n, k)
        s = ''
        for i in range(max_index-1, -1, -1):
            s += str(n//(k**i))
            n = n%(k**i)
        return s
    
    num = jinsoo(n, k)
    nums = num.split('0')
    real_nums = []
    for i in range(len(nums)):
        if nums[i].isnumeric():
            real_nums.append(int(nums[i]))
    
    def check(num):
        ans = True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                ans = False
                break
        return ans
    
    for num in real_nums:
        if num != 1 and check(num):
            answer += 1
            
    return answer

