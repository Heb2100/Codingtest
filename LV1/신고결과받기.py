id_list = ["muzi", "frodo", "apeach", "neo"]
test = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

id_list_report = [0 for i in id_list]
id_test = [0 for i in test]
list_reported = []
answer = []
report = []


for a in test:
    report.append(a.split()[1])

temp_i = ''
temp_j = ''
i_index = 0
j_index = 0
for i in id_list:
    for j in report:
        if i == j:
            id_list_report[i_index] += 1
        if i == temp_i and j == temp_j:
            id_list_report[i_index] -= 1
        temp_j = j
        j_index += 1
    temp_i = i
    i_index += 1

i_index = 0
j_index = 0
for i in report:
    for j in id_list_report:
        if k <= id_list_report[i_index]:
            id_test[j_index] += 1
        j_index += 1
    i_index += 1
print(id_test)

# i_index = 0
# for i in id_list_report:
#     if i <= id_list_report[i_index]:
#         id_test[i_index] += 1
#     i_index += 1

# for i in id_list_report:
#     if i >= k:
#         list_reported.append(i)

# print(list_reported)

# for i in list:
#     for j in list_reported:
#         if list[i][1] == j:
#             answer.append(list[i][0])

# a = 0
# for i in id_list:
#     for j in input:
#         if i == j:
#             id_list_ans[a] += 1
#     a += 1

# print(report)