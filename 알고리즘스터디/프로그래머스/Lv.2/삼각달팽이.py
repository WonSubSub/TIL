def solution(n):
    answer = []
    nums = [[0] * (x+1) for x in range(n)]
    numsum = sum([(x+1) for x in range(n)])
    number = 1
    start = 0
    end = n
    x = 1
    while number != numsum+1:
        for i in range(start, end): 
            nums[i][x-1] = number
            number += 1
            if number == numsum+1:
                break
        for i in range(x, end - x): 
            nums[end-1][i] = number     
            number += 1
            if number == numsum+1:
                break
        for i in range(end-1, start, -1):    
            nums[i][i-x+1] = number   
            number += 1
            if number == numsum+1:
                break
        start += 2
        end -= 1
        x += 1
    for num in nums:
        answer.extend(num)
    return answer
