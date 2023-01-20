def solution(files):
    answer = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz .-'
    all_file = []
    
    for i in range(len(files)):
        head = ''
        number = ''
        tail = ''
        numover = 0
        for s in range(len(files[i])):
            a = files[i][s]
            if a.lower() in alphabet:
                if numover == 1:
                    tail = files[i][s:]
                    break
                else:
                    head += a
            elif a.isnumeric():
                numover = 1
                number += a
                if len(number) == 5 and s != len(files[i])-1:
                    tail = files[i][s+1:]
                    break
        all_file.append([head, number, tail])
    all_file.sort(key= lambda x: (x[0].lower(), int(x[1])))
    
    for file in all_file:
        answer.append(''.join(file))
    
    return answer