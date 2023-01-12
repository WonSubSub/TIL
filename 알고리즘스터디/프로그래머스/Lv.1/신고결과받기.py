def solution(id_list, report, k):
    answer = []
    
    report_cnt = {}
    report_name = {}
    
    for i in id_list:
        report_name[i] = []
        
    for s in report:
        reporter, reported = s.split()
        if reported not in report_name[reporter]:
            report_name[reporter].append(reported)
            if reported not in report_cnt.keys():
                report_cnt[reported] = 1
            else:
                report_cnt[reported] += 1
    
    for reported in report_name.values():
        temp_answer = 0
        for s in reported:
            if report_cnt[s] >= k:
                temp_answer += 1
        answer.append(temp_answer)          
    
    return answer