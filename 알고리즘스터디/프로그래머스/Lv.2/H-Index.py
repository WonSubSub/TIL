def solution(citations):
    answer = len(citations)
    
    citations.sort(reverse=True)
    
    for i in range(len(citations)):
        if i+1 >= citations[i]:
            if len(citations) - i - 1 <= citations[i]:
                if citations[i-1] >= i:
                    answer = max(citations[i], i)
                    break
                else:
                    answer = citations[i]
                    break
    
    return answer