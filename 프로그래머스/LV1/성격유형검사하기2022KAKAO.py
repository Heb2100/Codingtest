def solution(survey, choices):
    R=0;C=0;J=0;A=0;
    i = 0
    temp = []
    for choice in survey:
        if choice == "RT":
            R += 4-choices[i]
        if choice == "TR":
            R += -(4-choices[i])
        if choice == "CF":
            C += 4-choices[i]
        if choice == "FC":
            C += -(4-choices[i])
        if choice == "JM":
            J += 4-choices[i]
        if choice == "MJ":
            J += -(4-choices[i])
        if choice == "AN":
            A += 4-choices[i]
        if choice == "NA":
            A += -(4-choices[i])
        i += 1
    if R>=0:
        temp.append('R')
    else:
        temp.append('T')
    if C>=0:
        temp.append('C')
    else:
        temp.append('F')
    if J>=0:
        temp.append('J')
    else:
        temp.append('M')
    if A>=0:
        temp.append('A')
    else:
        temp.append('N')
    answer = temp[0]+temp[1]+temp[2]+temp[3]
    return answer