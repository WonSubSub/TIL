def solution(arr):
    
    def get_min(num1, num2):
        mul = 1
        for i in range(min(num1, num2), 1, -1):
            if num1 % i == 0 and num2 % i == 0:
                mul = i
                break
        return int((num1 * num2) / mul)
    
    for i in range(1, len(arr)):
        arr[i] = get_min(arr[i-1], arr[i])
    
    answer = arr[-1]
                    
    return answer