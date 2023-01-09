def solution(nums):
    answer = 0
    if int(len(nums)/2) < len(set(nums)):
        answer = int(len(nums)/2)
    else:
        answer = len(set(nums))
                     
    return answer