def solution(participant, completion):
    answer_list = set(participant) - set(completion)
    if len(answer_list):
        answer = list(answer_list)[0]
    else:
        participant.sort()
        completion.sort()
        for i in range(len(participant)):
            if i == len(participant) - 1:
                answer = participant[-1]
            else:
                if participant[i] != completion[i]:
                    answer = participant[i]
                    break
        
        # for s in participant:
        #     if participant.count(s) > completion.count(s):
        #         answer = s
        #         break
    
    return answer