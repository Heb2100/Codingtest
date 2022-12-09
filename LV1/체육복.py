n = 3
lost = [3]
reserve = [1]
gym_num = [1 for i in range(n+1)]

for i in lost:
    gym_num[i-1] -= 1

for i in reserve:
    gym_num[i-1] += 1


for idx, i in enumerate(gym_num):
    if i == 0:
        if gym_num[idx-1] == 2:
            gym_num[idx-1] -= 1
            gym_num[idx] += 1
        else:
            if gym_num[idx+1] == 2:
                gym_num[idx+1] -= 1
                gym_num[idx] += 1
print(n- gym_num.count(0))