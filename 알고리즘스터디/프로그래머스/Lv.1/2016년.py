def solution(a, b):
    answer = ''
    days = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    day_count = b-1
    for i in range(1,a):
        day_count += days[i]
    day_string = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    
    answer_index = day_count % 7
    answer = day_string[answer_index]
    
    return answer