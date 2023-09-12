import sys, math
a = int(sys.stdin.readline())
answer_1 = []
for i in range(a):
    l = list(map(int, input().split()))
    answer_1.append(l)

def number_of_measure_and_smallest_div(input):
    answer = 0
    smallest_div = 0
    for i in range(1, math.ceil(math.sqrt(input+1))):
        if input % i == 0:
            if smallest_div == 0 and i != 1:
                smallest_div = i
            answer += 2
        if input == i*i:
            answer = answer - 1
    return [answer, smallest_div]

for i in range(a):
    if abs(answer_1[i][0]-answer_1[i][1]) >= 1:
        if answer_1[i][1] >= 4:
            if answer_1[i][1] % 2 == 1:
                print(2, answer_1[i][1]-3)
            else:
                print(2, answer_1[i][1]-2)
        else:
            print(-1)
    else:
        if number_of_measure_and_smallest_div(answer_1[i][0])[0] <= 2:
            print(-1)
        else:
            print(number_of_measure_and_smallest_div(answer_1[i][0])[1], answer_1[i][0]-number_of_measure_and_smallest_div(answer_1[i][0])[1])
