def solution(numbers, target):
    answer = []
    
    numbers.sort()
    target = int((sum(numbers) - target)/2)
    start = 0
    
    def dfs(numbers, target, start, answer):
        for i in range(start, len(numbers)):
            temp_target = target
            if temp_target >= numbers[i]:
                temp_target -= numbers[i]
                start += 1
                if temp_target == 0:
                    answer.append(1)
                else:
                    dfs(numbers, temp_target, start, answer)
            else:
                break
        return answer
    
    answer = dfs(numbers, target, start, answer)
    answer = sum(answer)
    return answer