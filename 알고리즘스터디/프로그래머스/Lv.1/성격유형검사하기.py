def solution(survey, choices):
    answer = ''
    
    scores = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0 }
    plus = [0, 3, 2, 1, 0, -1, -2, -3]
    
    for i in range(len(survey)):
        scores[survey[i][0]] += plus[choices[i]]
    
    if scores['R'] >= scores['T']:
        answer += 'R'
    else:
        answer += 'T'
        
    if scores['C'] >= scores['F']:
        answer += 'C'
    else:
        answer += 'F'
    
    if scores['J'] >= scores['M']:
        answer += 'J'
    else:
        answer += 'M'
    
    if scores['A'] >= scores['N']:
        answer += 'A'
    else:
        answer += 'N'
    
    return answer