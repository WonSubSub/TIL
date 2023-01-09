def solution(nums):
    answer = 0
    
    def check(num):
        b = True
        for i in range(2,int(num/2)):
            if num % i == 0:
                b = False
                break
        return b
    
    for i in range(len(nums)):
        for a in range(i+1, len(nums)):
            for b in range(a+1, len(nums)):
                num = nums[i] + nums[a] + nums[b]
                if check(num):
                    answer += 1
    
    return answer