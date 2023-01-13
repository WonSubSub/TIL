def solution(n, k):
    answer = []
    
    a = 1
    nums = []
    nums_mul = []
    for i in range(1,n+1):
        nums.append(i)
        a = a * i
        nums_mul.append(a)
        
    nums_mul.pop()
    nums_mul.sort(reverse=True)

    for i in nums_mul:
        if int(k%i) == 0:
            print(i)
            answer.append(nums[int(k//i)-1])
            nums.remove(nums[int(k//i)-1])
            answer.extend(nums[::-1])
            break
        else:
            answer.append(nums[int(k//i)])
            nums.remove(nums[int(k//i)])
            k = int(k%i)
    return answer