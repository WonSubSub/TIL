def solution(record):
    answer = []
    
    id_dict = {}
    str_list = []
    for s in record:
        s_list = s.split()
        id_dict[s_list[1]] = 1
        if s_list[0] == "Enter":
            str_list.append(s_list[1] + "님이 들어왔습니다.")
        elif s_list[0] == "Leave":
            str_list.append(s_list[1] + "님이 나갔습니다.")
    
    record = record[::-1]
    for s in record:
        s_list = s.split()
        if id_dict[s_list[1]] == 1 and s_list[0] != 'Leave':
            id_dict[s_list[1]] = s_list[2]
    
    for i in range(len(str_list)):
        str_list[i] = str_list[i].replace(str_list[i].split('님')[0], id_dict[str_list[i].split('님')[0]])
    answer = str_list
    
    return answer